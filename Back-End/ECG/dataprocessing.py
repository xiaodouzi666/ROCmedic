import os
import json

# 设置数据文件夹路径
data_folder = '/home/azuki/ECG/data'

# 定义心电图标签
categories = {
    "ECG Images of Myocardial Infarction Patients": "Myocardial Infarction detected.",
    "ECG Images of Patient that have abnormal heartbeat": "Abnormal heartbeat detected.",
    "ECG Images of Patient that have History of MI": "History of Myocardial Infarction detected.",
    "Normal Person ECG Images": "This ECG is normal and there are no abnormal symptoms."
}

# 定义统一的提示词
prompt = "Is there anything abnormal on this ECG?"

# 初始化结果列表
results = []

# 遍历每个类别文件夹
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

# 生成JSON文件
output_file = 'ecg_data.json'
with open(output_file, 'w') as f:
    json.dump(results, f, indent=4)

print(f"JSON文件已生成: {output_file}")
