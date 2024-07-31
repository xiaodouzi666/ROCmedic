from flask import Flask, request, jsonify, render_template_string
import os
import subprocess

app = Flask(__name__)

UPLOAD_FOLDER = '/home/azuki/Biochemical/VisualGLM-6B/upload_images'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Image Upload</title>
    </head>
    <body>
        <form id="uploadForm" enctype="multipart/form-data">
            <input type="file" id="fileInput" name="file">
            <button type="submit">上传图片</button>
        </form>
        <div>
            <h2>诊断结果：</h2>
            <p id="diagnosisResult"></p>
            <h2>病情建议：</h2>
            <p id="suggestion"></p>
        </div>

        <script>
            document.getElementById('uploadForm').addEventListener('submit', async function(event) {
                event.preventDefault();
                const fileInput = document.getElementById('fileInput');
                const formData = new FormData();
                formData.append('file', fileInput.files[0]);

                const response = await fetch('/upload', {
                    method: 'POST',
                    body: formData
                });

                const result = await response.json();
                document.getElementById('diagnosisResult').innerText = result.diagnosis_result || '无结果';
                document.getElementById('suggestion').innerText = result.suggestion || '无建议';
            });
        </script>
    </body>
    </html>
    ''')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filename)
        # 调用VisualGLM进行推理
        result = run_visualglm_inference(filename)
        return jsonify(result)

def run_visualglm_inference(image_path):
    # 调用cli_fit_flask.py进行推理
    command = f"python cli_fit_flask.py --image_path {image_path} --simplified --english"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    # 调试输出
    print(f"Subprocess output: {result.stdout}")
    print(f"Subprocess error: {result.stderr}")

    # 提取推理结果
    output_lines = result.stdout.split('\n')
    inference_output = []
    capturing = False
    for line in output_lines:
        if 'Number of text tokens' in line:
            capturing = True
            continue
        if capturing:
            inference_output.append(line.strip())

    if not inference_output:
        return {'error': 'Failed to extract inference output'}

    # 将推理结果合并为单个字符串
    diagnosis_result = " ".join(inference_output)
    suggestion = "根据诊断结果生成的建议"  # 示例建议

    return {
        'diagnosis_result': diagnosis_result,
        'suggestion': suggestion
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
