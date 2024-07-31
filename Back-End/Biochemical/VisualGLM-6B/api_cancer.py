from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import subprocess

app = Flask(__name__)
CORS(app)  # 允许所有来源的跨域请求

UPLOAD_FOLDER = '/home/azuki/Biochemical/VisualGLM-6B/upload_images'
PRETRAINED_MODEL_PATH = '/home/azuki/Biochemical/VisualGLM-6B/checkpoints/finetune-visualglm-6b-07-26-22-31'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/bio-upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filename)
        # 调用诊断接口
        diagnosis_result = get_diagnosis(filename)
        if 'error' in diagnosis_result:
            return jsonify(diagnosis_result)

        # 调用建议接口
        suggestion_result = get_suggestion(diagnosis_result['diagnosis_result'])
        if 'error' in suggestion_result:
            return jsonify(suggestion_result)

        return jsonify({
            'diagnosis_result': diagnosis_result['diagnosis_result'],
            'suggestion': suggestion_result['suggestion']
        })

@app.route('/bio-diagnosis', methods=['POST'])
def diagnosis():
    data = request.json
    image_path = data.get('image_path')
    if not image_path or not os.path.exists(image_path):
        return jsonify({'error': 'Invalid image path'}), 400
    return get_diagnosis(image_path)

def get_diagnosis(image_path):
    command = f"python cli_cancer.py --image_path {image_path} --from_pretrained {PRETRAINED_MODEL_PATH} --english"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(f"Subprocess output: {result.stdout}")
    print(f"Subprocess error: {result.stderr}")

    output_lines = result.stdout.split('\n')
    inference_output = []
    capturing = False
    for line in output_lines:
        if 'Number of text tokens' in line:
            capturing = True
            continue
        if capturing and not line.startswith('Welcome to BreastCancerGLM model'):
            inference_output.append(line.strip())

    if not inference_output:
        return {'error': 'Failed to extract inference output'}

    diagnosis_result = " ".join(inference_output).replace("Yes, ", "")
    return {
        'diagnosis_result': diagnosis_result
    }

@app.route('/bio-suggestion', methods=['POST'])
def suggestion():
    data = request.json
    diagnosis_result = data.get('diagnosis_result')
    if not diagnosis_result:
        return jsonify({'error': 'Invalid diagnosis result'}), 400
    return get_suggestion(diagnosis_result)

def get_suggestion(diagnosis_result):
    command = f'python cli_cancer.py --image_path "" --english'
    query = f'{diagnosis_result}\nPlease provide detailed judgment basis and directly answer what can be diagnosed with this breast tumor Xray image, and disease suggestion based on your diagnosis results. Please strictly follow the following format:\n\nJudgment basis:\n1. Please list the first basis\n2. Please list the second basis\n\nDisease suggestion:\n1. Please list the first suggestion\n2. Please list the second suggestion\n\nPlease make sure each basis and suggestion is on a separate line and listed according to the number.'
    print(f"Query sent to model: {query}")  # 调试输出
    result = subprocess.run(command, input=query, shell=True, capture_output=True, text=True)
    print(f"Subprocess output: {result.stdout}")
    print(f"Subprocess error: {result.stderr}")

    output_lines = result.stdout.split('\n')
    inference_output = []
    capturing = False
    for line in output_lines:
        if 'Number of text tokens' in line:
            capturing = True
            continue
        if capturing and not line.startswith('Welcome to BreastCancerGLM model'):
            cleaned_line = line.replace("User:", "").strip()
            inference_output.append(cleaned_line)

    if not inference_output:
        return {'error': 'Failed to extract inference output'}

    suggestion = " ".join(inference_output).replace("The breast tumor in this picture looks benign.", "").replace("The breast tumor in this picture looks malignant.", "")
    return {
        'suggestion': suggestion
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
