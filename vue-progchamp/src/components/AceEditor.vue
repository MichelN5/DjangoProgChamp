<template>


<div class="div">
<div class="codecon border border-primary rounded">

<div id="editor">
</div>

</div>

<div class="row my-2">


    <div id="cons"  class=" mx-2 col-12 border border-primary rounded"  :style="{ backgroundColor: 'white', height: '10em', color: outputColor, overflow: 'auto', maxWidth: '98.5%' }">
      <pre class="m-2 text-start">{{ codeoutput }}</pre>
    </div>
    <div class="col-2">

    </div>


</div>

        <div class="row">
            
    <p v-if="iscomplete" class="col-4" style="color:green">Challenge completed</p >
    <p v-else class="col-4"> Challenge not completed</p>
    <button type="button" class=" btn btn-primary my-3 col-3" @click="toSolution">Solution</button>
    <button type="button" class=" btn btn-primary my-3 mx-3 col-3" @click="CheckCode">Check</button>

        </div>





</div>







</template>

<script>


import *  as editor from '../assets/ace.js'
import * as mode from '../assets/mode-js.js'
import * as themecobalt from '../assets/theme-cobalt.js'
import axios from 'axios'





export default {


    data(){
        return {
            editor: '',
            codeoutput: '',
            outputColor: 'red',
            challenge:'',

            comchallenges: [],
            iscomplete: false,


        }

    },


    async mounted(){

      const category_slug = this.$route.params.category_slug
      const product_slug = this.$route.params.product_slug


      await axios.get(`challenges/${category_slug}/${product_slug}/`)
      .then(request=>{
        this.challenge= request.data
      }).catch(error =>{
        console.log(error)
      })

        this.editor= window.ace.edit("editor");
        this.editor.session.setMode("ace/mode/python");
        this.editor.setTheme("ace/theme/cobalt");
        this.editor.setValue(this.challenge.default_code || '', -1)


        this.editor.setOptions({
          
            fontSize: '13pt',
        });


    if (this.$store.state.isAuthenticated) {
    await axios.get('usercomch/')
    .then(request=>{
        this.comchallenges= request.data
    }).catch(error=>{
        console.log(error)
    })

    this.comchallenges.forEach(chall => {

        if (chall.challenge.id== this.challenge.id){
            this.iscomplete= true
        }
    })
    }



    },



    methods:{


        async CheckCode(){


                    const language = this.languageForChallenge()

                    const usercode = this.editor.getValue();
                    const addedcode= this.challenge.testcases_code || ''

                    await axios.post('run-code/', {
                        code: `${usercode}\n${addedcode}`,
                        language,
                    })
                    .then(response =>{      
                            if (response.data.success){
                                this.outputColor='green'
                                this.codeoutput = response.data.output || 'All checks passed.'

                                if (!this.iscomplete && this.$store.state.isAuthenticated){
                                axios.post('/completedchallenges/', {"challenge":this.challenge.id})
                                .then(request =>{
                                    console.log(request)
                                    this.iscomplete= true
                                }).catch(e=>{
                                    console.log(e)
                                })

                    

                                }
                            }
                            else{
                                this.outputColor ='red'
                                this.codeoutput = response.data.error || response.data.output || 'Checks failed.'
                            }
 
                    })
                    .catch(error => {
                        this.outputColor = 'red'
                        this.codeoutput = error.response?.data?.error || error.response?.data?.detail || 'Unable to run code. Log in and try again.'
                    })
      

                




        },

        toSolution(){
                const category_slug = this.$route.params.category_slug
                const product_slug = this.$route.params.product_slug
                this.$router.push(`/challenge/${category_slug}/${product_slug}/solution`)
        },

        languageForChallenge(){
            const slug = this.challenge?.Category?.slug
            if (slug === 'python') {
                return 'python'
            }
            if (slug === 'cpp') {
                return 'cpp'
            }
            return 'python'
        }

     
            

        }
    
}
</script>

<style type="text/css" media="screen" scoped>

    .codecon {
        width:100%;
        height: 500px;
    }

    #editor { 
        position: relative;
        height:100%;
        width:100%;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
    }
</style>
