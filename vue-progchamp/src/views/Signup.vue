<template>




<div class="d-flex justify-content-center my-3">

    <div class="row row-cols-1 border border-light rounded" style="background-color:White;max-width:80%;">

        <div class="col my-3"><h1>Sign up</h1></div>
        
        <div class="col">
            <div class="alert alert-danger" role="alert" v-if="errors.length">
                <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>
        </div>

        <div class="col">

            <div class="mb-3">
  <label  class="form-label">  Username</label>
  <input v-model="username" class="form-control" >
</div>
            <div class="mb-3">
  <label  class="form-label">  Password</label>
  <input type="password" v-model="password" class="form-control" >
</div>
            <div class="mb-3">
  <label  class="form-label">  Repeat password</label>
  <input type="password" v-model="password2" class="form-control" >
</div>

<div class="d-flex justify-content-start mx-3" style="color:green" ><a @click="this.$router.push('/log-in/')" >Log in</a></div>
<div class="d-flex justify-content-end mx-5 mb-3">
    <button type="button" class="btn btn-primary" @click="SubmitSignup">Sign up</button>

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
            password:'',
            username:'',
            password2:'',
            errors:[]
        }
    },
    methods: {
        SubmitSignup(){
            this.errors= []
            if(this.username===''){
                this.errors.push('The username is missing')
            }
            if (this.password === '') {
                this.errors.push('The password is too short')
            }
            if (this.password !== this.password2) {
                this.errors.push('The passwords doesn\'t match')
            }
            if (!this.errors.length) {
                let formData = {
                    username: this.username,
                    password: this.password
                }

                        axios.post("/api/users/", formData)
        .then(reponse=> {
            this.$router.push('/log-in')
        })
        .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again')
                            
                            console.log(JSON.stringify(error))
                        }
                    })
            

        }


    }

}
}
</script>