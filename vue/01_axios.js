var vm = new Vue({
    el: '#app',
    data: {
        books: [],
    },
    methods: {
      fn(){
          var url = "http://127.0.0.1:8000/books/?page=3";
          axios.get(url)
              .then(response => {
                  this.books = response.data;
              })
              .catch(error => {
                  console.log(error.response.data);
              })
      },
    },
});