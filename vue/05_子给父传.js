var child = {
    template: "<div><a href='#' @click='send_to_parent'>子组件</a></div>",
    data(){
        return {
            abc: 123,
        }
    },
    methods: {
        send_to_parent(){
            this.$emit("send", 'abc', 'lll');
        },
    },
};

Vue.component("parent", {
    template: "<div>父组件<child @send='receive_from_child'></child>父组件</div>",
    components: {
        child,
    },
    data(){
        return{
            count: 100,
        }
    },
    methods: {
        receive_from_child(param1,param2){
            alert(param1+param2);
        },
    },
});


var vm = new Vue({
   el: "#app",
});