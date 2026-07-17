<template>
<div class="container my-4" id="cont">
<div class="accordion" id="accordionPanelsStayOpenExample">
  <div class="accordion-item">
    <h2 class="accordion-header" id="panelsStayOpen-headingOne">
      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseOne" aria-expanded="true" aria-controls="panelsStayOpen-collapseOne">
        Instructions
      </button>
    </h2>
    <div id="panelsStayOpen-collapseOne" class="accordion-collapse collapse show" aria-labelledby="panelsStayOpen-headingOne">
      <div class="accordion-body" id="instructions">

      </div>
    </div>
  </div>
  <div class="accordion-item">
    <h2 class="accordion-header" id="panelsStayOpen-headingTwo">
      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseTwo" aria-expanded="false" aria-controls="panelsStayOpen-collapseTwo">
        Code
      </button>
    </h2>
    <div id="panelsStayOpen-collapseTwo" class="accordion-collapse collapse" aria-labelledby="panelsStayOpen-headingTwo">
      <div class="accordion-body">


            <AceEditor />

      
      </div>
    </div>
  </div>
  
</div>

</div>


</template>




<script>
import AceEditor from '../components/AceEditor.vue'
import axios from 'axios'


export default {

    data(){
      return {
        challenge:[],
      }
    },
    components:{ AceEditor },

    async mounted(){
      const category_slug = this.$route.params.category_slug
      const product_slug = this.$route.params.product_slug


      await axios.get(`challenges/${category_slug}/${product_slug}/`)
      .then(request=>{
        this.challenge= request.data
      }).catch(error =>{
        console.log(error)
      })
      const result = this.challenge.Description.split('\n').join('<br>');
      let ins= document.getElementById('instructions')
      ins.innerHTML= result

    }
    
}
</script>

<style>

#cont{
  text-align: center;
}

</style>>
