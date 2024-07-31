
<template>
  <div class="el-image--wrap">
    <IUpload @handleUploadChange="handleUploadChange" class="el-upload--mask"/>

    <div class="demo-image__preview">
        <el-image
            class="demo-image"
            :src="store.uploadSrc || imageSrc"
            :zoom-rate="1.2"
            :max-scale="7"
            :min-scale="0.2"
            :preview-src-list="previewList"
        >
          <template #error>
            <div style="color: #fff">
              <!-- 点击上传图片 -->
              <el-icon color="#fff" size="40px"><Plus /></el-icon>
            </div>
          </template>

        </el-image>

    </div>
  </div>
</template>
  
<script setup lang="ts">
  import { ref, watch } from 'vue'
  import { genFileId, ElLoading } from 'element-plus'
  import type { 
    UploadInstance, 
    UploadProps, 
    UploadRawFile,
    UploadFile,
    UploadFiles
} from 'element-plus'
import Upload from './upload.vue'
import { useScanStore } from '../stores'
import { storeToRefs } from 'pinia'
  
const store = useScanStore()
const { uploadScanImage, updateUploadSrc } = store

const upload = ref<UploadInstance>()
const previewList = ref<string[]>([])
const loadingRef = ref()
const imageSrc = ref<string>('')

// watch(store, (newVal, oldVal) => {
//   console.log('store.uploadSrc', newVal, oldVal)
//   // imageSrc.value = store.uploadSrc
// })

const handleExceed: UploadProps['onExceed'] = (files) => {
  upload.value!.clearFiles()
  const file = files[0] as UploadRawFile
  file.uid = genFileId()
  // upload.value!.handleStart(file)
}

const handleUploadChange = (src: string) => {
  // uploadSrc.value = ''
  console.log('uploadFile', src)
  // uploadSrc.value = src
  imageSrc.value = src
  updateUploadSrc(src)
  previewList.value = [src]

  // uploadScanImage(src)
}

const submitUpload = () => {
  upload.value!.submit()
}

const openLoading = () => {
  loadingRef.value = ElLoading.service({
    lock: true,
    text: 'Loading',
    background: 'rgba(0, 0, 0, 0.7)',
  })
}

const closeLoading = () => {
  loadingRef.value?.close?.()
}
</script>

<style>
.el-image--wrap{
    position: relative;
    height: 100%;
    background: #484848;
    border-radius: 4px;
    overflow: hidden;
    /* 十六进制值:#313236; rgb 代码值：rgb(49,50,54) */
}
.el-upload--mask,
.demo-image__upload{
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  z-index: 100;
}
.demo-image__preview{
  --el-card-border-radius: 4px;
  display: flex;
  height: 100%;
  justify-content: center;
  align-items: center;
  position: relative;
  border-radius: var(--el-card-border-radius);
  overflow: hidden;
  margin: auto;
}
.demo-image__upload{
  /* display: none; */
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 100;
}
.demo-image__preview:hover .demo-image__upload{
  display: block;
}
.demo-image{
  border-radius: var(--el-card-border-radius);
}
@media screen and (max-width: 1450px) {
  .demo-image{
    /* margin-top: -200px; */
  }
}

</style>
  