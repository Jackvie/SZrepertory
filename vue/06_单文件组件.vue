<template>
    <div>哈哈{{ count }}</div>
</template>

<script>
    export default {
        data(){
            return {
                count: 1,
            }
        },
    };
</script>

<style scoped>
    div {
        font-size: 2em;
        text-align: center;
    }
</style>
