<template>
    <div class="d-flex justify-content-center my-3">

    <div class="row row-cols-1 border border-light rounded" style="background-color:White;max-width:80%;">

        <div class="col my-3"><h1>Log in</h1></div>
        
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

<div class="d-flex justify-content-start mx-3" style="color:green" ><a @click="this.$router.push('/signup/')" >Sign up</a></div>

<div class="d-flex justify-content-end mx-5 mb-3">
    <button type="button" class="btn btn-primary" @click="SubmitLogin">Log in</button>

</div>




        </div>



        
    </div>

</div>
</template>

<script>
import axios from 'axios'
export default {
     data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Log In'
    },
    methods: {
        async SubmitLogin () {
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("token")
            const formData = {
                username: this.username,
                password: this.password
            }
            await axios
                .post("/api/token/login/", formData)
                .then(response => {
                    const token = response.data.auth_token
                    this.$store.commit('setToken', token)
                    
                    axios.defaults.headers.common["Authorization"] = "Token " + token
                    localStorage.setItem("token", token)
                   
                    this.$router.push('/')
                    
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    } else {
                        this.errors.push('Something went wrong. Please try again')
                        
                        console.log(JSON.stringify(error))
                    }
                })

        }
}
}
</script>