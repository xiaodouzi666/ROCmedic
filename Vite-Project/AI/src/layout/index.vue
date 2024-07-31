<template>
    <div class="common-layout">
      <el-container class="common-layout">
        <el-aside width="200px">
            <Sidebar />
        </el-aside>
        <el-main class="el-main--extra">
            <router-view />
        </el-main>
      </el-container>
    </div>
</template>

<script lang="ts" setup>
  import { ref } from 'vue'
  import {
    Document,
    Menu as IconMenu,
    Location,
    Setting,
  } from '@element-plus/icons-vue'
  import Sidebar from './sidebar.vue';

  
  const isCollapse = ref(true)
  const handleOpen = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
  }
  const handleClose = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
  }
</script>
<style>
.common-layout{
    --el-menu-bg-color: #303030;
    --el-menu-border-color: #181818;
    height: 100%;
}
.el-main--extra{
  overflow: hidden;
  padding: 0 var(--el-main-padding);
}
</style>