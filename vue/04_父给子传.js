var child = {
    template: "<div>子组件{{ num1 }}&nbsp;{{ num2 }}</div>",
    props: ['num1', 'num2'],
};


Vue.component('parent',{
    template: "<div>父组件<child :num1=count1 :num2=count2></child>父组件</div>",
    // template: "<div>父组件<child :num1='count1' :num2='count2'></child>父组件</div>",
    components: {
        child,
    },
    data(){
        return {
            count1: 100,
            count2: 200,
        }
    },
});


// 创建Vue对象
var vm = new Vue({
    // 接管app对象对应的div区域
    el: "#app",
});