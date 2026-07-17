<template>


<div>

<h3 style="text-align:center">Searching for {{query}}</h3>




<div class="container" id="cont2">

<div class="row">
  

  <div v-for="challenge in challenges" v-bind:key="challenge.id" class="col-lg-4 col-md-6 my-1">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">{{challenge.Title}}</h5>
        <p class="card-text">{{challenge.Category.CategoryName}}</p>
        <a href="#" class="btn btn-primary" @click="this.$router.push(`/challenge/${challenge.Category.slug}/${challenge.slug}`)">Begin</a>
      </div>
    </div>
  </div>


  </div>
</div>
</div>
    
</template>

<script>
import axios from 'axios'
export default {
    data(){
        return {
            query: '',
            challenges: []
        }

    },

    mounted(){
            document.title= "Search"
            let uri = window.location.search.substring(1)
            let params = new URLSearchParams(uri)
             if (params.get('query')) {
            this.query = params.get('query')
            this.performSearch()
        }
        },
         methods: {
        async performSearch() {
            console.log(this.query)
            await axios
                .post('/search/', {"query" : this.query})
                .then(response => {
                    this.challenges = response.data
                })
                .catch(error => {
                    console.log(error)
                })

        }
         }

    
}
</script>
