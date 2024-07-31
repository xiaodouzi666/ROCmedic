import os
import json

def filter_nonexistent_images(json_path, image_folder):
    # 读取 JSON 文件
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 筛查存在的图片
    filtered_data = [item for item in data if os.path.exists(item['image'])]

    # 保存过滤后的 JSON 文件
    with open('filtered_data.json', 'w', encoding='utf-8') as f:
        json.dump(filtered_data, f, ensure_ascii=False, indent=4)

    print(f"原始数据条目数: {len(data)}, 过滤后数据条目数: {len(filtered_data)}")

# 示例路径
json_path = '/home/azuki/Biochemical/formatted_data.json'
image_folder = '/home/azuki/Biochemical/data/images'

filter_nonexistent_images(json_path, image_folder)
