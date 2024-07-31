import json

# 读取 JSON 文件
with open('/home/azuki/Biochemical/data/images/formatted_data.json', 'r') as file:
    data = json.load(file)

# 遍历每条数据并添加诊断建议
for item in data:
    if "benign" in item["label"]:
        item["diagnostic_suggestion"] = "This breast tumor is benign and there is no need to worry too much, but it should be checked regularly."
    elif "malignant" in item["label"]:
        item["diagnostic_suggestion"] = "This breast tumor is malignant, please seek medical attention immediately for further examination and treatment."

# 将更新后的数据写回 JSON 文件
with open('/home/azuki/Biochemical/data/images/formatted_data.json', 'w') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
