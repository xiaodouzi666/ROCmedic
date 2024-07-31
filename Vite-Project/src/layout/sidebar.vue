<template>
    <el-menu
      :default-active="activeMenu"
      class="el-menu-vertical"
      text-color="#D8D8D8"
      :collapse="isCollapse"
      router
      @open="handleOpen"
      @close="handleClose"
    >
      <el-menu-item :index="item.path" v-for="(item, index) in menuList">
        <!-- <el-icon><icon-menu /></el-icon> -->
        <template #title>
          {{ t(item.title) }}
        </template>
      </el-menu-item>
    <!-- <el-menu-item>
      <div @click="toggleI18n">切换语言</div>
    </el-menu-item> -->
    </el-menu>
  </template>
  
<script lang="ts" setup>
import { ref, computed, watch } from 'vue'
import { useRoute } from 'vue-router';
import { useScanStore } from '../stores'
import {useI18n} from 'vue-i18n'
import i18n from '../i18n'

const { t } = useI18n()
const { resetState } = useScanStore()
const route = useRoute()
const menuList = ref([
  {
      title: 'menu.xray',
      path: '/xray'
  },
  {
      title: 'menu.pathological',
      path: '/pathological'
  },
  {
      title: 'menu.electrocardiogram',
      path: '/electrocardiograph'
  },
  // {
  //     title: '诊断历史',
  //     path: '/history'
  // }
])
const isCollapse = ref(false)
const activeMenu = computed(() => route.path)

watch(activeMenu, (newVal, oldVal) => {
  if(newVal !== oldVal) {
    resetState()
  }
})
const handleOpen = (key: string, keyPath: string[]) => {
  resetState()
}
const handleClose = (key: string, keyPath: string[]) => {
  
}

const toggleI18n = () => {
  console.log('切换语言', i18n.global.locale)
  i18n.global.locale =  i18n.global.locale === 'zh' ? 'en' : 'zh'
}

</script>
  
  <style>
  .el-menu-vertical{
    --el-menu-hover-bg-color: #505050;
    height: 100%;
  }
  .el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 200px;
    min-height: 400px;
  }
  </style>
  