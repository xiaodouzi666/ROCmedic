import json

input_path = '/home/azuki/XrayGLM/data/Xray/openi-zh.json'
output_path = '/home/azuki/XrayGLM/data/Xray/openi-zh-new.json'

with open(input_path, 'r', encoding='utf-8') as infile:
    data = json.load(infile)

new_data = []
for item in data['annotations']:
    new_item = {
        "img": f"/home/azuki/XrayGLM/data/Xray/{item['image_id']}.png",
        "caption": item['caption'],
        "prompt": "\u8bf7\u8be6\u7ec6\u63cf\u8ff0\u8fd9\u5f20X\u5149\u7247\u7684\u8bca\u65ad\u7ed3\u679c\u3002",  # 请详细描述这张X光片的诊断结果。
        "label": item['caption']
    }
    new_data.append(new_item)

with open(output_path, 'w', encoding='utf-8') as outfile:
    json.dump(new_data, outfile, ensure_ascii=True, indent=4)

print("转换完成")
