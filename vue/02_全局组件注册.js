Vue.component('login', {
    template: '<div>登录组件内容</div>',
});

var vm = new Vue({
    el: '#app',
    data: {
        count: "",
    },
    methods: {
      fn(){
         var url = "";
         axios.get(url)
              .then(response => {
                  console.log(response.data);
              })
              .catch(error => {
                  console.log(error.response.data);
              })
      },
    },
});