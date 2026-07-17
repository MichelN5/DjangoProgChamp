<template>


<div class="container" id="cont2">
<h2 class="my-3">{{ pageTitle }}</h2>

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

  <p v-if="!challenges.length" class="my-4">No challenges found for this category yet.</p>


  </div>
</div>




</template>

<script>
import axios from 'axios'
export default {

  data(){
    return {
      challenges:[],
    }
  },
  computed: {
    pageTitle(){
      const category = this.$route.params.category_slug
      if (!category) {
        return 'All Challenges'
      }
      return `${category.charAt(0).toUpperCase()}${category.slice(1)} Challenges`
    }
  },
  mounted(){
    this.loadChallenges()
  },
  watch: {
    '$route.params.category_slug'(){
      this.loadChallenges()
    }
  },
  methods: {
    loadChallenges(){
      const category = this.$route.params.category_slug
      const url = category ? `challenges/?category=${category}` : 'challenges/'
      axios.get(url)
    .then(request=>
    this.challenges= request.data)
    .catch(error =>{
      console.log(error)
    })
    }
  }

}
</script>

<style>
#cont2 {
  text-align: center;
}
</style>
