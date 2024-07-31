#!/bin/bash

#  api_ecg.py
echo "Starting ECG API on port 5001..."
nohup python /home/azuki/ECG/VisualGLM-6B/api_ecg.py > ecg.log 2>&1 &

#  api_xray.py
echo "Starting X-ray API on port 5000..."
nohup python /home/azuki/Xray/api_xray.py > xray.log 2>&1 &

#  api_cancer.py
echo "Starting Cancer API on port 5002..."
nohup python /home/azuki/Biochemical/VisualGLM-6B/api_cancer.py > cancer.log 2>&1 &

echo "All APIs have been started."

