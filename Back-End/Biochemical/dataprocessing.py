import os
import pydicom
import json
import numpy as np
from PIL import Image
import pandas as pd

def convert_dicom_to_png(dicom_file, output_file):
    dicom_data = pydicom.dcmread(dicom_file)
    pixel_array = dicom_data.pixel_array

    # If the pixel array is 3D, take the middle slice
    if len(pixel_array.shape) == 3:
        pixel_array = pixel_array[pixel_array.shape[0] // 2]

    # Normalize the pixel array
    pixel_array = (pixel_array - pixel_array.min()) / (pixel_array.max() - pixel_array.min())
    pixel_array = (pixel_array * 255).astype(np.uint8)

    image = Image.fromarray(pixel_array)
    image.save(output_file)

def extract_metadata_from_dicom(dicom_folder, metadata_df):
    extracted_data = []

    for root, dirs, files in os.walk(dicom_folder):
        for file in files:
            if file.endswith(".dcm"):
                file_path = os.path.join(root, file)
                dicom_data = pydicom.dcmread(file_path)
                patient_id = dicom_data.PatientID
                metadata_entry = metadata_df[metadata_df['Patient ID'] == patient_id].to_dict(orient='records')

                if metadata_entry:
                    metadata_entry = metadata_entry[0]
                    metadata_entry["dicom_path"] = file_path
                    image_file_name = os.path.join("/home/azuki/Biochemical/data/images", file.replace('.dcm', '.png'))
                    metadata_entry["image_path"] = image_file_name

                    # Check tumor/benign status
                    for i in range(1, 7):  # Assuming up to 6 tumors/benign fields
                        tumor_field = f'tumor/benign{i}'
                        if tumor_field in metadata_entry:
                            if metadata_entry[tumor_field] == 1:
                                metadata_entry['tumor_status'] = 'malignant'
                                break
                            elif metadata_entry[tumor_field] == 0:
                                metadata_entry['tumor_status'] = 'benign'
                                break
                    else:
                        metadata_entry['tumor_status'] = 'unknown'

                    convert_dicom_to_png(file_path, metadata_entry["image_path"])
                    extracted_data.append(metadata_entry)
    
    return extracted_data

# 示例路径
dicom_folder = '/home/azuki/NFS/manifest-1713182663002/Advanced-MRI-Breast-Lesions'
metadata_path = '/home/azuki/Biochemical/Advanced-MRI-Breast-Lesions-DA-Clinical-Jan112024.xlsx'

# 使用第二行作为列名读取 Excel 文件
metadata_df = pd.read_excel(metadata_path, header=1)

# 查看数据框架中的列名
print(metadata_df.columns)

# 提取 DICOM 元数据
extracted_data = extract_metadata_from_dicom(dicom_folder, metadata_df)

# 保存到JSON文件
with open('extracted_data.json', 'w') as f:
    json.dump(extracted_data, f, indent=4)
