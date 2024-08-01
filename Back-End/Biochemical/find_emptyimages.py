import os
import json

def filter_nonexistent_images(json_path, image_folder):
    # Reading JSON Files
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Screening for existing images
    filtered_data = [item for item in data if os.path.exists(item['image'])]

    # Save the filtered JSON file
    with open('filtered_data.json', 'w', encoding='utf-8') as f:
        json.dump(filtered_data, f, ensure_ascii=False, indent=4)

    print(f"原始数据条目数: {len(data)}, 过滤后数据条目数: {len(filtered_data)}")


json_path = '/home/azuki/Biochemical/formatted_data.json'
image_folder = '/home/azuki/Biochemical/data/images'

filter_nonexistent_images(json_path, image_folder)
