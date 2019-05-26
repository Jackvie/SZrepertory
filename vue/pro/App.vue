<template>
    <!-- 组件模板内容 -->
    <div>
        单文件组件：{{ content }}
        <!-- 路由组件占位符，根据路由规则加载对应的组件内容 -->
        <router-view></router-view>
    </div>
</template>

<script>
    // js内容
    export default {
        data: function () {
            return {
                content: 'hello world!'
            }
        }
    }
</script>

<style scoped>
   /* css样式 */
</style>