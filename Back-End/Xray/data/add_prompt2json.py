import json

with open('/home/azuki/XrayGLM/data/Xray/openi-zh-new.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    if 'prompt' not in item:
        item['prompt'] = "请详细描述这张X光片的诊断结果。"  # 或者其他默认值

with open('/home/azuki/XrayGLM/data/Xray/openi-zh-new.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
