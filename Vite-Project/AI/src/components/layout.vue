<template>
  <el-row class="el--row">
    <el-col :span="16">
      <slot name="left" />
    </el-col>
    <div class="el-col--gap"></div>
    <el-col :span="7.5" style="flex: 1">
      <slot name="right">
        <!-- <div class="flex flex-column">
          <Card class="flex-item" title="扫描结果：" :content="store.scanResult"></Card>
          <Card class="flex-item" title="病情建议：" :content="store.suggestion"></Card>
        </div> -->
        <el-tabs v-model="activeName" class="tabs-list" @tab-click="handleClick">
          <el-tab-pane :label="t('tab.scanResult')" name="scanResult">
            <div class="tab-item--content">{{ store.scanResult }}</div>
          </el-tab-pane>
          <el-tab-pane :label="t('tab.suggestion')" name="suggestion">
            <div class="tab-item--content">{{ store.suggestion }}</div>
          </el-tab-pane>
          <el-tab-pane :label="t('tab.history')" name="history">
            <div class="tab-item--content">
              <div class="history">
                  <div :class="activeId === item.id ? 'history-item history-item--active' : 'history-item'" 
                  v-for="(item, index) in historyList"
                  :key="item.id"
                  @click="() => handleViewHistory(item)"
                >
                  <div>{{ item.title }}</div>
                  <div class="history-delete-icon">
                    <el-icon @click.stop="() => handleDeleteItem(item.id)"><Delete /></el-icon>
                  </div>
                </div>
              </div>
            </div>
          </el-tab-pane>
        </el-tabs>
      </slot>
    </el-col>
  </el-row>
</template>


<script setup>
import { ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import { liveQuery } from "dexie";
import { useObservable } from "@vueuse/rxjs";
import { useI18n } from 'vue-i18n';
import { useScanStore, getStorageByKey } from '../stores';
import {
  queryXrayDb,
  orderBy,
  db,
  queryPathologicalDb,
  queryElectrocardiographDb
} from '../stores/db'

import {
  XRAY_STORAGE_KEY,
  PATHO_STORAGE_KEY,
  ELECTRO_STORAGE_KEY,
} from '../constants'

const { t } = useI18n()
defineProps({
  msg: {
    type: String,
    required: false
  }
})

const route = useRoute()
const store = useScanStore()
const activeName = ref('scanResult')
const historyList = ref([])
const activeId = ref()

watch(useObservable(
  liveQuery(() => db.xray.toArray())
), (newVal) => {
  historyList.value = orderBy(newVal)
})

watch(useObservable(
  liveQuery(() => db.pathological.toArray())
), (newVal) => {
  historyList.value = orderBy(newVal)
})

watch(useObservable(
  liveQuery(() => db.electrocardiograph.toArray())
), (newVal) => {
  historyList.value = orderBy(newVal)
})

const handleClick = (tab) => {
  activeName.value = tab
}


watch(activeName, (newVal, oldVal) => {
  
  let storageKey = XRAY_STORAGE_KEY;
  if(newVal === 'history') {
    queryDb()
  }
})

const queryDb = () => {
  const routePath = route.path.slice(1)
  switch(routePath) {
    case 'xray':
      queryXrayDb().then(res => {
        historyList.value = res
      })
      break;
    case 'pathological':
      queryPathologicalDb().then(res => {
        historyList.value = res
      })
      break;
    case 'electrocardiograph':
      queryElectrocardiographDb().then(res => {
        historyList.value = res
      })
      break;
  }
}

const handleViewHistory = (item) => {
  store.updateStore(item)
  activeId.value = item.id
  activeName.value = 'scanResult'
}

const handleDeleteItem = (id) => {
  const routePath = route.path.slice(1)
  switch(routePath){
    case 'xray':
      db.xray.delete(id)
      break;
    case 'pathological':
      db.pathological.delete(id)
      break;
    case 'electrocardiograph':
      db.electrocardiograph.delete(id)
      break;
  }
  if(activeId.value === id) {
    store.resetState()
  }
  queryDb()
}
</script>

<style>
.tabs-list .el-tabs__item {
  padding: 0 20px 0 0;
}
</style>
<style scoped>
.flex{
    display: flex;
    height: 100%;
}
.flex-column{
    --el-border-color-light: #303030;
    flex-direction: column;

}
.flex-item{
    --el-card-bg-color: #303030;
    flex: 1;
    /* background: #303030 !important; */
    color: #fff;
    overflow: hidden;
}
.el--row{
  display: flex;
  flex-wrap: nowrap;
  width: 100%;
  height: 100%;
}
.el-col--gap{
  width: var(--el-main-padding);
}

.tabs-list{
  --el-text-color-primary: #fff;
  --el-border-color-light: transparent;
  color: #fff;
  overflow: hidden;
}

.tab-item--content{
  height: calc(100vh - 75px);
  overflow-y: scroll;
}
.history{
  padding: 0 0 30px 0;

}
.history-item{
  width: 200px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
}
.history-item--active,
.history-item:hover{
  /* background: #484848; */
  color: var(--el-menu-active-color)
}
.history-delete-icon{
  display: flex;
  align-items: center;
  cursor: pointer;
  /* padding: 0 0 0 20px; */
}
</style>
