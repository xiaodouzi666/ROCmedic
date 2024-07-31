<template>

    <Layout>
        <template #left>
            <Image />
        </template>
        <!-- <template #right>
            <div class="flex flex-column">
                <Card class="flex-item"></Card>
                <Card class="flex-item" title="病情建议："></Card>
            </div>
            
        </template> -->
    </Layout>

</template>
<script setup>

</script>

<style>
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
</style>