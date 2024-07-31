<template>
    <el-card 
        style="max-width: 500px"
        body-class="el-card--body"
        >
      <template #header>
        <div class="card-header">
          <h1>{{ props.title }}</h1>
        </div>
      </template>
      <div class="el-card--content">{{ content }}</div>
      
    </el-card>
  </template>

<script setup>
import { defineProps } from 'vue';

const props = defineProps({
    title: {
        type: String,
        default: '诊断结果：'
    },
    content: {
      type: String,
      default: ''
    }
})
</script>

<style>
.el-card--body{
    display: inline-block;
    /* height: 82%; */
    padding: 0 var(--el-card-padding);
    overflow-y: scroll
}
.el-card--content{
    height: 300px;
    overflow: scroll;
    word-wrap: break-word;
    word-break: break-all;
}

@media screen and (min-width: 1920px) {
  .el-card--content {
    font-size: 20px;
  }
}
</style>