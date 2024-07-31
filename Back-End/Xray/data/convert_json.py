import json
import os

# 加载原始 JSON 文件
with open('/home/azuki/XrayGLM/data/Xray/openi-zh.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 转换后的列表
new_data = []

for item in data['annotations']:
    image_path = f"/home/azuki/XrayGLM/data/Xray/{item['image_id']}.png"
    if not os.path.exists(image_path):
        print(f"Warning: {image_path} does not exist.")
    new_item = {
        'img': image_path,
        'caption': item['caption']
    }
    new_data.append(new_item)

# 保存为新的 JSON 文件
with open('/home/azuki/XrayGLM/data/Xray/openi-zh-new.json', 'w', encoding='utf-8') as f:
    json.dump(new_data, f, ensure_ascii=False, indent=4)
