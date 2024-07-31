<template>
    <!-- <div class="history"> -->
        <el-row class="history-wrap">
            <el-col :span="4">
                <div class="history">
                    <div class="history-list">
                        <div class="history-item" v-for="item in 60">{{ item }}</div>
                    </div>
                </div>
            </el-col>

            <el-col :span="20">
                <Layout>
                    <template #left>
                        <el-image
                            src="https://pinia.vuejs.org/logo.svg"
                            :zoom-rate="1.2"
                            :max-scale="7"
                            :min-scale="0.2"
                        />
                    </template>
                    <template #right>
                        <!-- <div class="flex flex-column">
                            <Card class="flex-item" title="扫描结果：" :content="scanResult"></Card>
                            <Card class="flex-item" title="病情建议：" :content="suggestion"></Card>
                        </div> -->
                        <el-tabs v-model="activeName" class="tabs-list" @tab-click="handleClick">
                            <el-tab-pane label="扫描结果" name="scanResult">
                                <div class="tab-item--content">{{ scanResult }}</div>
                            </el-tab-pane>
                            <el-tab-pane label="病情建议" name="suggestion">
                                <div class="tab-item--content">{{ suggestion }}</div>
                            </el-tab-pane>
                        </el-tabs>
                    </template>
                </Layout>
            </el-col>
        </el-row>
    <!-- </div> -->
</template>
<script setup>
import { ref } from 'vue'
const content = `6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer
6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer
6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer
6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer
6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer
6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer
6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer
6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer
6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer
6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer
6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer
6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer
6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer
6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer
6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer
6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer6awefgwergw regwer gwer gwer`


const scanResult = ref(content)
const suggestion = ref(content)

const activeName = ref('scanResult')

const handleClick = (tab) => {
  activeName.value = tab
}

</script>

<style>
.history-wrap{
    background: #484848;
}
.history{
    height: calc(100vh - 40px);
    overflow-y: scroll;
}
.history-list {
    color: #D8D8D8;
    
    /* border-right: 1px solid #181818; */
}
.history-item {
    cursor: pointer;
    padding: 0 10px;
    height: 30px;
}
.history-item:hover{
    background: #505050;
}
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
.tabs-list{
  --el-text-color-primary: #fff;
  --el-border-color-light: transparent;
  color: #fff;
  /* height: calc(100vh - 40px); */
  overflow-y: scroll;
}
.tab-item--content{
  height: calc(100vh - 75px);
  overflow-y: scroll;
}
</style>