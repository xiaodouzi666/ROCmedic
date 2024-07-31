import json

# 读取 JSON 文件
with open('/home/azuki/XrayGLM/data/Xray/openi-zh-new.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 遍历所有项目，添加 label 字段
for item in data:
    if 'label' not in item:
        item['label'] = item['caption']  # 将 caption 字段的值赋给 label

# 保存更新后的 JSON 文件
with open('/home/azuki/XrayGLM/data/Xray/openi-zh-new.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("JSON 文件已更新，label 字段已添加。")
