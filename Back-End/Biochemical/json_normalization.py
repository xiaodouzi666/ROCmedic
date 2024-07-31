import json

def convert_json(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile:
        data = json.load(infile)
        
    converted_data = []
    for item in data:
        new_item = {
            "id": item["id"],
            "prompt": "Is the breast tumor in this picture benign or malignant?",
            "label": f"The breast tumor in this picture looks {item['text']}.",
            "image": item["image"]
        }
        converted_data.append(new_item)
        
    with open(output_path, 'w', encoding='utf-8') as outfile:
        json.dump(converted_data, outfile, indent=4)

# 输入和输出文件路径
input_path = "/home/azuki/Biochemical/data/images/formatted_data.json"
output_path = "/home/azuki/Biochemical/data/images/converted_data.json"

convert_json(input_path, output_path)
