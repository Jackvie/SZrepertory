// 引入vue和app组件
import Vue from 'vue'
import App from './App.vue'

// 导入定义好的路由
import router from './router/router.js'

// 导入ElementUI插件
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

// 在vue中使用Element-UI插件
Vue.use(ElementUI);

new Vue({
    el: "#app",
    router: router,
    render: function (create) {
        return create(App);
    },

});