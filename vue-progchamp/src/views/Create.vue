<template>
<div>
    <h2 style="text-align:center" class="my-3">Create Challenge</h2>

    <div class="container border border-light rounded mb-4 my-2" style="background-color:white; ">
    
    <div class="row  my-2">

        <div class="col">
            <label >Title</label>
            <input type="text" class="form-control" v-model="title" placeholder="Title">
        </div>

        <div class="col ">
            <label >Category</label>
            <select class="form-select" v-model="category">

                 <option value="1">PY</option>
                 <option value="3">C++</option>
            </select>
        </div>


        <div class="row my-2">
            <div class="col">
                <label>Description</label>
                <textarea v-model="description" class="form-control"  rows="7"></textarea>
            </div>
        </div>

        
        <div class="row my-2s">
            <div class="col">
                <label>Solution</label>
                <textarea v-model="solution" class="form-control"  rows="7"></textarea>
            </div>
        </div>

        <div class="row my-2">
            <div class="col">
                <label>Default Code</label>
                <textarea v-model="defcode" class="form-control"  rows="7"></textarea>
            </div>
        </div>

        <div class="row my-2">
            <div class="col">
                <label>Test Cases Code</label>
                <textarea v-model="testcode" class="form-control"  rows="7"></textarea>
            </div>
        </div>

        

        <div class="row">
            <div class="col">
                <label>Slug</label>
                <input type="text" class="form-control" v-model="slug" placeholder="Slug">
            </div>

            <div class="col d-flex justify-content-center mt-3">
                <button class="btn btn-primary" @click="sumbitForm" >Create</button>
            </div>
        </div>
    </div>

    <div class="alert alert-danger" role="alert" v-if="errors.length">
                <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>


</div>
</div>
</template>


<script>
import axios from 'axios'
export default {
    data(){
        return {
            title: '',
            category: '',
            description: '',
            solution: '',
            defcode: '',
            testcode: '',
            slug: '',
            errors: [],
            data: {},
            user: [],
        }
    },

    async mounted(){

        await axios.get('getuser')
        .then(request=>{    
            this.user= request.data[0]
            

        })
        .catch(error=>
        {
            console.log(error)
        })
    },

    methods: {
        async sumbitForm(){
            this.errors = []
            if (this.title === '') {
                this.errors.push('The title field is missing!')
            }
            if (this.category === '') {
                this.errors.push('The category field is missing!')
            }
            if (this.description === '') {
                this.errors.push('The description is missing!')
            }

            if (this.solution === '') {
                this.errors.push('The solution field is missing!')
            }
            
            
            if (this.defcode === '') {
                this.errors.push('The default code  field is missing!')
            }

            if (this.testcode === '') {
                this.errors.push('The test code field is missing!')
            }
            
            
            if (this.slug === '') {
                this.errors.push('The slug  field is missing!')
            }

            if(!this.errors.length){
                const data= {
                    'Category': parseInt(this.category),
                    'Title': this.title,
                    'Description': this.description,
                    'Solution': this.solution,
                    'slug': this.slug,
                    'default_code': this.defcode,
                    'testcases_code': this.testcode,
                    'Created_by': this.user.id,
                }

            this.data= data

            await axios
                .post('/create/', data).
                then(request=>{
                    console.log(request)
                    this.$router.push('/successcr')
                })
                .catch(error=>
                {
                  console.log(error)
                })
                
            }
        }
        
    }
}
</script>