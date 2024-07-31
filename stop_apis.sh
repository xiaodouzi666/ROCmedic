#!/bin/bash

# Find and stop the process of api_ecg.py
echo "Stopping ECG API..."
pkill -f api_ecg.py

# Find and stop the process of api_xray.py
echo "Stopping X-ray API..."
pkill -f api_xray.py

# Find and stop the process of api_cancer.py
echo "Stopping Cancer API..."
pkill -f api_cancer.py

echo "All APIs have been stopped."

