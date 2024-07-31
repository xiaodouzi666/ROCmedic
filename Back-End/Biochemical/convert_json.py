import json

# 读取原始的 JSON 文件
with open('/home/azuki/Biochemical/extracted_data.json', 'r') as f:
    data = json.load(f)

# 创建新的格式化的 JSON 数据
formatted_data = []

for entry in data:
    if entry['tumor_status'] != 'unknown':  # 只保留肿瘤状态已知的数据
        formatted_entry = {
            "id": entry["Patient ID"],
            "text": entry["tumor_status"],
            "image": entry["image_path"]
        }
        formatted_data.append(formatted_entry)

# 将新的 JSON 数据保存到文件
with open('formatted_data.json', 'w') as f:
    json.dump(formatted_data, f, indent=4)

print("Formatted data has been saved to formatted_data.json")
