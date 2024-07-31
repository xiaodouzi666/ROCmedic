from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import torch
from transformers import AutoTokenizer
from sat.model.mixins import CachedAutoregressiveMixin
from model import VisualGLMModel, chat
from finetune_visualglm import FineTuneVisualGLMModel
from sat.model import AutoModel
import argparse

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from all sources

UPLOAD_FOLDER = '/home/azuki/ECG/VisualGLM-6B/upload_images'
PRETRAINED_MODEL_PATH = '/home/azuki/ECG/VisualGLM-6B/checkpoints/finetune-visualglm-6b-07-28-08-39/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Preload the model
model, tokenizer = None, None

# Diagnostic result keyword dictionary
diagnosis_keywords = [
    "Myocardial Infarction detected.",
    "Abnormal heartbeat detected.",
    "History of Myocardial Infarction detected.",
    "This ECG is normal."
]

def load_model():
    global model, tokenizer
    print("Loading model...")
    model, model_args = FineTuneVisualGLMModel.from_pretrained(
        PRETRAINED_MODEL_PATH,
        args=argparse.Namespace(
            fp16=True,
            skip_init=True,
            use_gpu_initialization=True if (torch.cuda.is_available()) else False,
            device='cuda' if (torch.cuda.is_available()) else 'cpu',
        ),
        url='local'
    )
    model = model.eval()
    model.add_mixin('auto-regressive', CachedAutoregressiveMixin())
    tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True)
    print("Model loaded successfully.")

@app.route('/ecg-upload', methods=['POST'])
def upload_file():
    print("Received request.")
    if 'file' not in request.files:
        print("No file part.")
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        print("No selected file.")
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filename)
        print(f"File saved: {filename}")
        # Call the diagnostic interface
        diagnosis_result = get_diagnosis(filename)
        if 'error' in diagnosis_result:
            print("Error in diagnosis.")
            return jsonify(diagnosis_result)

        print("Diagnosis completed.")
        return jsonify({
            'diagnosis_result': diagnosis_result['diagnosis_result'],
            'suggestion': diagnosis_result['suggestion_text']
        })

def get_diagnosis(image_path):
    print(f"Running diagnosis on image: {image_path}")
    with torch.no_grad():
        history = None
        cache_image = None
        query = "What can be diagnosed with this ECG image?"
        try:
            response, history, cache_image = chat(
                image_path, 
                model, 
                tokenizer,
                query, 
                history=history, 
                image=cache_image, 
                max_length=2048, 
                top_p=0.4, 
                temperature=0.8,
                top_k=100,
                english=True,
                invalid_slices=[slice(63823, 130000)]
            )
        except Exception as e:
            print(e)
            return {'error': 'Failed to extract inference output'}

        diagnosis_result = response.split('Agent:')[-1].strip()
        
        # Separate diagnostic results and diagnostic suggestions
        diagnosis = None
        for keyword in diagnosis_keywords:
            if keyword in diagnosis_result:
                diagnosis = keyword
                suggestion_text = diagnosis_result.split(keyword)[-1].strip()
                break
        
        if not diagnosis:
            return {'error': 'Failed to extract diagnosis result'}

        return {
            'diagnosis_result': diagnosis,
            'suggestion_text': suggestion_text
        }

if __name__ == '__main__':
    load_model()  # Preload the model
    print("Starting Flask server...")
    app.run(host='0.0.0.0', port=5000)
