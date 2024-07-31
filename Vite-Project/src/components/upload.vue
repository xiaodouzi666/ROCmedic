
<template>
    <div class="el-upload--wrap">
        <img class="upload-demo--bg" src="/upload2.gif" v-show="showGif"/>
        <el-upload
            ref="upload"
            class="upload-demo"
            action="#"
            list-type="picture-card"
            :on-change="handleUploadChange"
            :auto-upload="false"
            :show-file-list="false"
            >
            <template #trigger>
                <el-button type="primary">上传图片</el-button>
            </template>
        </el-upload>
    </div>
</template>
  
<script setup lang="ts">
  import { ref, defineEmits, computed } from 'vue'
  import { useRoute } from 'vue-router'
  import { genFileId } from 'element-plus'
  import type { 
    UploadInstance, 
    UploadProps, 
    UploadRawFile,
    UploadFile,
    UploadFiles
} from 'element-plus'

import { useScanStore } from '../stores'
import { storeToRefs } from 'pinia'

const { 
  uploadXray, 
  uploadPathological,
  uploadElectrocardiograph,
  updateUploadSrc,
  resetState,
} = useScanStore()
const { uploadSrc } = storeToRefs(useScanStore())
const route = useRoute()
const emits = defineEmits(['handleUploadChange'])

  const upload = ref<UploadInstance>()
  // const uploadSrc = ref()
  const previewList = ref<string[]>([])
  const isUpload = ref(false)

  const showGif = computed(() => !uploadSrc || !isUpload.value)

  const saveImageToCurrentFolder = (imageUrl, fileName) => {
    // 使用a标签下载图片
    const link = document.createElement('a');
    link.href = imageUrl;
    link.download = fileName;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
};

  const getBase64 = (file) => {
      return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = (e) => {
          resolve(reader.result)
          // // 创建一个Blob对象，并设置其内容为文件的DataURL
          // const imgBlob = new Blob([e.target.result], { type: file.type });
          
          // // 创建一个新的URL指向Blob对象
          // const imgUrl = URL.createObjectURL(imgBlob);
          
          // // 这里可以将imgUrl用于展示，或者保存到本地
          // saveImageToCurrentFolder(imgUrl, file.name);
        };
        reader.onerror = error => reject(error);
      });
    };

  const handleUploadChange = (uploadFile: UploadFile, uploadFiles: UploadFiles) => {
    // console.log('uploadFile', uploadFile)
    // console.log('uploadFiles', route.path.slice(1))
    isUpload.value = true
    
    getBase64(uploadFile.raw).then((res) => {
      console.log(src, '上传文件的src--base64',res)
      const path = route.path.slice(1)
      const formdata = new FormData()

      
      formdata.append('file', uploadFile.raw!)
      if(path === 'xray') {
        uploadXray(formdata, res)
      }
      if(path === 'pathological') {
        uploadPathological(formdata, res)
      }
      if(path === 'electrocardiograph') {
        uploadElectrocardiograph(formdata, res)
      }
    })
    const src = URL.createObjectURL(uploadFile.raw!)
    console.log(src, '上传文件的src',)
    // uploadSrc.value = src
    previewList.value = [src]

    updateUploadSrc(src)
    

    emits('handleUploadChange', src)
  }
  
  const submitUpload = () => {
    upload.value!.submit()
  }
  </script>

<style>
.upload-demo,
.upload-demo button {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    height: 100%;
    opacity: 0;
    z-index: 10;
}
.upload-demo--bg{
  position: relative;
  z-index: -1;
  width: 100%;
  height: 100%;
}
</style>
  