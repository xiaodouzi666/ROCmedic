from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import subprocess

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from all sources

UPLOAD_FOLDER = '~/ECG/VisualGLM-6B/upload_images'
PRETRAINED_MODEL_PATH = '/home/azuki/ECG/VisualGLM-6B/checkpoints/finetune-visualglm-6b-07-28-08-39/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/ecg-upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filename)
        # Call the diagnostic interface
        diagnosis_result = get_diagnosis(filename)
        if 'error' in diagnosis_result:
            return jsonify(diagnosis_result)

        # Call the suggestion interface
        suggestion_result = get_suggestion(diagnosis_result['diagnosis_result'])
        if 'error' in suggestion_result:
            return jsonify(suggestion_result)

        return jsonify({
            'diagnosis_result': diagnosis_result['diagnosis_result'],
            'suggestion': suggestion_result['suggestion']
        })

def get_diagnosis(image_path):
    command = f"python cli_ecg.py --image_path {image_path} --from_pretrained {PRETRAINED_MODEL_PATH} --prompt_en 'What can be diagnosed with this ECG image?'"
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
        if capturing and not line.startswith('Welcome to ECG model'):
            inference_output.append(line.strip())

    if not inference_output:
        return {'error': 'Failed to extract inference output'}

    diagnosis_result = " ".join(inference_output)
    
    # Separate diagnostic results and diagnostic suggestions
    diagnosis = diagnosis_result.split('。')[0]  # Get the first sentence as the diagnosis result
    suggestions = diagnosis_result.split('。')[1:]  # Get the rest as diagnostic suggestions
    suggestion_text = "。".join(suggestions).strip()

    return {
        'diagnosis_result': diagnosis,
        'suggestion_text': suggestion_text
    }

def get_suggestion(diagnosis_result):
    command = f"python cli_ecg.py --image_path '' --english"
    query = f'{diagnosis_result}\nPlease provide detailed judgment on what can be diagnosed with this EKG image. Please strictly follow the following format:\n\nJudgment basis:\n1. Please list the first basis\n2. Please list the second basis\n\nDisease suggestion:\n1. Please list the first suggestion\n2. Please list the second suggestion\n\nPlease make sure each basis and suggestion is on a separate line and listed according to the number.'
    print(f"Query sent to model: {query}")
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
        if capturing and not line.startswith('Welcome to ECG model'):
            cleaned_line = line.replace("User:", "").strip()
            inference_output.append(cleaned_line)

    if not inference_output:
        return {'error': 'Failed to extract inference output'}

    suggestion = " ".join(inference_output).replace("Yes, that is correct.", "")
    return {
        'suggestion': suggestion
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
