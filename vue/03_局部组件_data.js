var login = {
    template: "<div>局部的{{ count }}组件</div>",
    data(){
        return {
            count: 10,
        }
    },
};

var vm = new Vue({
    el: '#app',
    data: {
        count: "",
    },
    components: {
        login,
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