import os
import json

# Set the data folder path
data_folder = '/home/azuki/ECG/data'

# Define ECG Labels
categories = {
    "ECG Images of Myocardial Infarction Patients": "Myocardial Infarction detected.",
    "ECG Images of Patient that have abnormal heartbeat": "Abnormal heartbeat detected.",
    "ECG Images of Patient that have History of MI": "History of Myocardial Infarction detected.",
    "Normal Person ECG Images": "This ECG is normal and there are no abnormal symptoms."
}

# Definition prompt word
prompt = "Is there anything abnormal on this ECG?"

# Initialize the result list
results = []

# Loop through each category folder
for category, label in categories.items():
    category_path = os.path.join(data_folder, category)
    if os.path.isdir(category_path):
        for image_name in os.listdir(category_path):
            if image_name.endswith(('.png', '.jpg', '.jpeg')):  # 只处理图片文件
                image_path = os.path.join(category_path, image_name)
                result = {
                    "id": image_name,
                    "prompt": prompt,
                    "label": label,
                    "image": image_path
                }
                results.append(result)

# Generate JSON file
output_file = 'ecg_data.json'
with open(output_file, 'w') as f:
    json.dump(results, f, indent=4)

print(f"JSON file generated: {output_file}")
