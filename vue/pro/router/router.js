import Vue from 'vue'
// 导入路由插件
import Router from 'vue-router'

import Child1 from '../components/Child1.vue'
import Child2 from '../components/Child2.vue'
import Button from '../components/Button.vue'


// 1. 在vue中使用路由插件
Vue.use(Router);

// 2. 定义路由规则
export default new Router({
    routes: [
        {
            path: '/',
            component: Child1
        },
        {
            path: '/child2',
            component: Child2
        },
        {
            path: '/button',
            component: Button
        },
    ]
})