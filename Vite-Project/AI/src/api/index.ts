import axios from 'axios';

// axios.defaults.baseURL = 'http://10.0.8.50:5000';
// axios.defaults.baseURL = 'http://localhost:5000';
// axios.defaults.headers.common['Authorization'] = 'AUTH_TOKEN';
axios.defaults.headers.post['Content-Type'] = 'multipart/form-data';

export const uploadScanImageApi = async (data) => {
    console.log('data',data)
    return await axios.post('/upload', {}, {

    })
}
// x光
export async function upload(formdata) {
    return await axios.post('http://10.0.8.50:5000/upload', formdata)
}

// 病理分析
export async function bioUpload(formdata) {
    return await axios.post('http://10.0.8.50:5002/bio-upload', formdata)
}

// 心电图
export async function ecgUpload(formdata) {
    return await axios.post('http://10.0.8.50:5001/ecg-upload', formdata)
}
