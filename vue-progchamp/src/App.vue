<template>





<div id="page-container">
  <div id="content-wrap">
      <header class="p-3 mb-3  border-bottom" style="">
    <div class="container">
      <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
        <a href="/" class="d-flex align-items-center mb-2 mb-lg-0 text-dark text-decoration-none">
           <img src="../src/assets/ProgChamp1.png" alt="" width="70" height="70" class="d-inline-block ">
        </a>

        <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
          <li><router-link to="/" class="nav-link px-2 link-dark">All</router-link></li>
          <li><router-link to="/category/python" class="nav-link px-2 link-dark">Python</router-link></li>
          <li><router-link to="/category/cpp" class="nav-link px-2 link-dark">C++</router-link></li>
  
        </ul>

        <form class="col-12 col-lg-auto mb-3 mb-lg-0 me-lg-3" role="search" method="get" action="/search" >
          <input type="search" class="form-control" placeholder="Search..." aria-label="Search" name="query">
        </form>

        <div class="dropdown text-end" v-if="$store.state.isAuthenticated">
          <a  href="#" class="d-block link-dark text-decoration-none dropdown-toggle" id="dropdownUser1" data-bs-toggle="dropdown" aria-expanded="false">
            <img v-if="profile_url" :src="profile_url" alt="" style="width:auto;height:auto;max-height:32px;" class="rounded-circle">
            <img v-else src="../src/assets/nouser.jpg" alt="aa" style="width:auto;height:auto;max-height:32px;" class="rounded-circle">

          </a>
          <ul class="dropdown-menu text-small" aria-labelledby="dropdownUser1">
            <li><a class="dropdown-item" href="#" @click="this.$router.push('/create')">Create Challenge...</a></li>
            <li><a class="dropdown-item" href="#" @click="this.$router.push('/myacc')">Profile</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#" @click="logout">Sign out</a></li>
          </ul>
        </div>



          <div class="dropdown text-end" v-else>
          <a  href="#" class="d-block link-dark text-decoration-none dropdown-toggle" id="dropdownUser1" data-bs-toggle="dropdown" aria-expanded="false">
            <img src="../src/assets/nouser.jpg" alt="aa" style="width:auto;height:auto;max-height:32px;" class="rounded-circle">
          </a>
          <ul class="dropdown-menu text-small" aria-labelledby="dropdownUser1">

            <li><a class="dropdown-item" href="#" @click="this.$router.push('/log-in')">Log in</a></li>
          </ul>
        </div>
      </div>
    </div>
      </header>

  <router-view/>

  </div>



  <footer id="footer" class="bg-light text-center text-lg-start ">
  <!-- Copyright -->
  <div class="text-center p-3" style="background-color: #face6e;">
    © 2022 Copyright
  </div>
  <!-- Copyright -->
</footer>

</div>


  
  
</template>


<script>
import axios from 'axios'
export default {
  data(){
    return {
      userprofile:[],
      profile_url:null,
    }
  },

    beforeCreate(){
    this.$store.commit('initializeStore')

    const token = this.$store.state.token
    if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }
  },

  async mounted(){
      if (!this.$store.state.isAuthenticated) {
        return
      }

         await axios.get('profile')
        .then(request=>{  

            if (request.data.length) {
              this.userprofile= request.data[0]
              this.profile_url= request.data[0].get_profile
            }

            

        })
        .catch(error=>
        {
            console.log(error)
        })
  },

  methods: {
            logout() {
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("token")
            localStorage.removeItem("username")
            localStorage.removeItem("userid")
            this.$store.commit('removeToken')
            this.$router.push('/')
        },
  }
  
}
</script>

<style lang="scss">
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
      
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  color: #2c3e50;
}


  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }

    #page-container {
  position: relative;
  min-height: 106vh;
  background: linear-gradient(40deg, #155263 9%, #155263 43%, #FF6F3C calc(43% + 1px), #FF6F3C 52%, #FF9A3C calc(52% + 1px), #FF9A3C 80%, #FFC93C calc(80% + 1px), #FFC93C 100%);
}

#content-wrap{
  padding-bottom: 2.5rem;    /* Footer height */
}

#footer {
  position: absolute;
  bottom: 0;
  width: 100%;
}


  @import '../node_modules/bootstrap/scss/bootstrap.scss';

</style>
