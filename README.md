# ROCmedic: 🥰Affordable AI Diagnostics For Everyone❤️

![12276c0f51b07dfa82402d82eb50dee](https://github.com/user-attachments/assets/5246e5d1-5cfb-47fa-871b-6b798aa53cc7)


## Reproduction Instructions

**Introduction:**
The following section provides detailed instructions for reproducing the data processing workflows used in ROCmedic. This includes steps for handling breast cancer, ECG, and X-ray imaging data, ensuring the data is in a suitable format for model training and fine-tuning.

![architecture](https://github.com/user-attachments/assets/dc369444-6612-4f26-beb0-7d28ece8daae)


### 1.1 Data Processing

**1.1.1 Breast Tumor Data**

1. **Data Acquisition**
   - Download the relevant data from the Cancer Imaging Archive website, which offers data downloaders for both Linux and Windows platforms.
   - Save the downloaded data onto your server or local machine. The data should appear as shown in the example below.

![Untitled 2](https://github.com/user-attachments/assets/3a05b943-6395-4517-81f0-a79b3ebc5da7)


1. **Data Processing**

   - Navigate to the specified directory using the command:

     ```bash
     cd Biochemical
     ```

   - Execute the following commands sequentially to process the data:

     ```bash
     python dataprocessing.py   # This step may take a considerable amount of time.
     python find_emptyimages.py
     python convert_json.py
     python json_normalization.py
     python add_suggestion.py
     ```

   - These scripts will convert DICOM files into trainable image formats, add labels and prompts, and include diagnostic suggestions. The final output will be JSON files ready for model fine-tuning.

   - Note: Due to the large volume of data (646GB), full-scale data training was not feasible on our server. Users with sufficient hardware resources are recommended to perform full data fine-tuning to achieve optimal model performance.

**1.1.2 ECG Data**

**Data Preparation**

- Navigate to the ECG data directory:

  ```bash
  cd ECG
  ```

- Execute the following commands to process the ECG data:

  ```bash
  python dataprocessing.py
  python add_suggestions_to_json.py
  ```

- These scripts will handle the data processing, transforming it into a format suitable for model training.

**1.1.3 X-ray Data**

**Data Handling**

- The X-ray data has been pre-processed and does not require additional steps.
- However, for those interested in the processing logic, reference the code within the Xray/data directory, which contains comprehensive data handling procedures.

### 1.2 Reproduction Process

This section outlines the steps required to reproduce and test the individual components of ROCmedic. It includes detailed instructions for debugging and running the application, ensuring that users can effectively replicate the processes for ECG, X-ray, and Breast Tumor analysis.

**1.2.1 Individual Debugging**

For debugging individual components, follow the steps below. Here, ECG analysis is used as an example.

1. **Navigate to the ECG Directory:**

   ```bash
   cd ECG/VisualGLM-6B
   ```

2. **Start the Backend Service:**
   Run the following command to initiate the backend service:

    ```bash
   python api_ecg.py
    ```

    Upon successful initiation, the backend service should display output indicating it is running on various addresses.

![Untitled 3](https://github.com/user-attachments/assets/49032968-a1d5-4ebe-94db-b397fe473169)


3. **Start the Frontend Service:**
   In the frontend directory, start the service using:

    ```bash
   serve -p 8080
    ```

    If `serve` is not installed, run `npm install serve` first. Upon successful start, the terminal should display the service running at local and network addresses.

    ![Untitled 4](https://github.com/user-attachments/assets/28c00a0d-c894-4581-a481-ad278a14a3b9)


4. **Access the Service in a Browser:**
   Open the specified local address (e.g., [http://localhost:8080](http://localhost:8080/)) in a web browser. Navigate to the ECG Analysis tab, upload an image, and view the returned results.

    ![Untitled 5](https://github.com/user-attachments/assets/b5233101-a3d9-4827-a6dd-061ea1aa6fcb)


    ![Untitled 6](https://github.com/user-attachments/assets/1d2dc1bf-b895-484f-9ec1-8e4136246172)


    The steps for debugging X-ray Diagnosis and Breast Tumor Analysis are similar. Ensure you select the appropriate project in the frontend during testing.

### 1.2.2 Full System Testing

1. **Start All APIs:**
   To initiate all services simultaneously, execute the following script:

    ```bash
   bash start_apis.sh
    ```

    Upon successful initiation, you should see a confirmation message indicating that all services are running.

    ![Untitled 7](https://github.com/user-attachments/assets/306942db-159a-4979-8148-1a3904b6891d)


2. **Access and Use the Services:**
   Open the web interface and interact with the three diagnostic services (ECG, X-ray, and Breast Tumor Analysis). Each service should be accessible and functional, allowing for simultaneous usage.

3. **Stop All APIs:**
   Once testing is complete, stop all running services using:

    ```bash
   bash stop_apis.sh
    ```

    This command will terminate all active services, ensuring that resources are freed.

By following these steps, users can effectively debug and test the individual components as well as the full system of ROCmedic, ensuring that all functionalities are operating as intended.

### PS: All the checkpoints files(.pt) can be found in Google Drive Link: https://drive.google.com/drive/folders/1FzqcNIGAykXaL-yM5MF45zPhWt5y9Yf2?usp=sharing
### Dataset need to be downloaded by yourself
