import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { 
  uploadScanImageApi,
  upload,
  bioUpload,
  ecgUpload
} from '../api'
import { ElLoading, ElMessage } from 'element-plus'
import {
  XRAY_STORAGE_KEY,
  PATHO_STORAGE_KEY,
  ELECTRO_STORAGE_KEY,
} from '../constants'
import { v4 as uuidv4 } from 'uuid';
import dayjs from 'dayjs'
import {
  addXrayDb,
  queryXrayDb,
  addPathologicalDb,
  queryPathologicalDb,
  addElectrocardiographDb,
  queryElectrocardiographDb
} from './db'

const content = `6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer
6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer
6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer
6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer
6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer
6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer
6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer
6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer`


function createStorageInfo(opts) {
  return {
    id: uuidv4(),
    title: dayjs().format('YYYY-MM-DD HH:mm:ss'),
    src: opts.src,
    scanResult: opts.scanResult,
    suggestion: opts.suggestion
  }
}

export function getStorageByKey(key) {
  const store = sessionStorage.getItem(key)
  if(!store) {
    return []
  }
  return JSON.parse(store)
}

export function setStorageByKey(key, stringValue) {
  sessionStorage.setItem(key, stringValue)
}

export const useScanStore = defineStore('counter', () => {

  const suggestion = ref(content)
  const scanResult = ref(content)
  const uploadSrc = ref('')
  const loadingRef = ref()

  const updateSuggestion = (val) => {
    suggestion.value = val
  }
  const updateScaneResult = (val) => {
    scanResult.value = val
  }
  const updateUploadSrc = (val) => {
    uploadSrc.value = val
  }

  const resetState = () => {
    updateSuggestion('')
    updateScaneResult('')
    updateUploadSrc('')
  }
  const updateStore = (store) => {
    console.log('更新', store)
    updateSuggestion(store.suggestion)
    updateScaneResult(store.scanResult)
    updateUploadSrc(store.src)
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

  const uploadScanImage = async (src, type) => {
    openLoading()
    resetState()
    console.log('uploadScanImage', src)

    try {
      const res = await uploadScanImageApi(src)
    } catch(error) {
      ElMessage.error(error.message)
    }finally {
      setTimeout(() => {
        closeLoading()
        updateSuggestion(content)
        updateScaneResult(content)
      }, 3000)
    }
  }

  const handleThen = (src, res) => {
    updateUploadSrc(src)
    updateSuggestion(res.suggestion || res.data.suggestion)
    updateScaneResult(res.diagnosis_result || res.data.diagnosis_result)

    closeLoading()
    const item = createStorageInfo({
      src,
      scanResult: res.diagnosis_result || res.data.diagnosis_result,
      suggestion: res.suggestion || res.data.suggestion
    })
    return item
  }

  const uploadXray = async (formdata, src) => {
    openLoading()
    resetState()
    
    try {
      const res = await upload(formdata)
      const errorMessage = res.error || res.data.error
      if(errorMessage) {
        ElMessage.error(errorMessage)
        return
      }
      if(res.diagnosis_result || res.data.diagnosis_result) {
        addXrayDb(handleThen(src, res))
      }
    } catch(error) {
      closeLoading()
      ElMessage.error(error.message)
    }finally {
      // setTimeout(() => {
      //   closeLoading()
      //   updateSuggestion(content)
      //   updateScaneResult(content)
      //   const item = createStorageInfo({
      //     src,
      //     scanResult: content,
      //     suggestion: content
      //   })
      //   addXrayDb(item)
      //   console.log('添加到indexedDB')
      // }, 20000)
    }
  }

  const uploadPathological = async (formdata, src) => {
    openLoading()
    resetState()
    
    try {
      const res = await bioUpload(formdata)
      const errorMessage = res.error || res.data.error
      if(errorMessage) {
        ElMessage.error(errorMessage)
        return
      }
      if(res.diagnosis_result || res.data.diagnosis_result) {
        addPathologicalDb(handleThen(src, res))
      }
    } catch(error) {
      closeLoading()
      ElMessage.error(error.message)
    }finally {
      // closeLoading()
      // updateSuggestion(content)
      // updateScaneResult(content)
      // const item = createStorageInfo({
      //   src,
      //   scanResult: content,
      //   suggestion: content
      // })
      // console.log('添加到indexedDB',addPathologicalDb(item))
    }
  }

  const uploadElectrocardiograph = async (formdata, src) => {
    openLoading()
    resetState()
    
    try {
      const res = await ecgUpload(formdata)
      const errorMessage = res.error || res.data.error
      if(errorMessage) {
        ElMessage.error(errorMessage)
        return
      }
      if(res.diagnosis_result || res.data.diagnosis_result) {
        addElectrocardiographDb(handleThen(src, res))
      }
    } catch(error) {
      closeLoading()
      ElMessage.error(error.message)
    }finally {
      // closeLoading()
      // updateSuggestion(content)
      // updateScaneResult(content)
      // const item = createStorageInfo({
      //   src,
      //   scanResult: content,
      //   suggestion: content
      // })
      // console.log('添加到indexedDB',addElectrocardiographDb(item))
    }
  }


  return {
    uploadSrc,
    suggestion,
    updateSuggestion,
    scanResult,
    updateScaneResult,
    uploadScanImage,
    uploadXray,
    resetState,
    updateStore,
    updateUploadSrc,
    uploadPathological,
    uploadElectrocardiograph
  }
})
