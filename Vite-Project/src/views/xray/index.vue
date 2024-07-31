<template>

        <Layout>
            <template #left>
                <Image />
            </template>
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