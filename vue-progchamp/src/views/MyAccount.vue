<template>


<div class="container my-4 profile-page">

    <div class="profile-card">

    <div class="row align-items-center g-3">

        <div class="col-12 col-md-4 d-flex align-items-center justify-content-center">

            <img v-if="profile_url" :src="profile_url" alt="" class="profile-image"
            data-bs-toggle="modal" data-bs-target="#exampleModal">

            <img v-else src="../assets/nouser.jpg" alt="" class="profile-image"
            data-bs-toggle="modal" data-bs-target="#exampleModal">
            






<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Update Profile</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <input type="file" @change="onFileChanged">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-danger" data-bs-dismiss="modal" @click="onDelete">Remove</button>
        <button type="button" class="btn btn-primary" @click="onUpload">Change Image</button>
      </div>
    </div>
  </div>
</div>

<!-- Modal -->
        </div>

        <div class="col">
            <p class="profile-label mb-1">Profile</p>
            <h1 class="profile-name">{{user.username}}</h1>
            <div class="profile-stats">
              <div class="stat-box">
                <span>{{comchall.length}}</span>
                Completed
              </div>
              <div class="stat-box">
                <span>{{crchall.length}}</span>
                Created
              </div>
            </div>


        </div>
    </div>

    </div>

    


    <div class="challenge-panel">
      <div class="challenge-panel-header">
        <div>
          <p class="profile-label mb-1">Challenges</p>
          <h3 class="mb-0">{{ activeTab === 'completed' ? 'Completed Challenges' : 'Created Challenges' }}</h3>
        </div>
        <div class="btn-group" role="group" aria-label="Profile challenge lists">
          <button type="button" class="btn" :class="activeTab === 'completed' ? 'btn-success' : 'btn-outline-secondary'" @click="showcomp">
            Completed
          </button>
          <button type="button" class="btn" :class="activeTab === 'created' ? 'btn-success' : 'btn-outline-secondary'" @click="showcr">
            Created
          </button>
        </div>
      </div>

      <div v-if="!shownchallenges.length" class="empty-state">
        No challenges to show yet.
      </div>

      <div v-else class="challenge-list">
        <button v-for="chall in shownchallenges" :key="chall.id" @click="RouteToChall(chall)" class="challenge-row">
          <span class="challenge-icon">{{ getChallengeInitial(chall) }}</span>
          <span class="challenge-info">
            <strong>{{ getChallengeTitle(chall) }}</strong>
            <small>{{ getChallengeCategory(chall) }}</small>
          </span>
          <span class="challenge-action">Open</span>
        </button>
      </div>
    </div>


    </div>

</template>




<script>
import axios from 'axios'
export default {

    data(){
        return {

            user : [],
            userprofile: [],
            comchall: [],
            crchall : [],
            shownchallenges: [],
            activeTab: 'completed',
            selectedFile: null,
            profile_url: '',

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
        


        await axios.get('usercomch/')
        .then(request=>{
            this.comchall= request.data
            this.shownchallenges = this.comchall
        })
        .catch(error=>
        {
            console.log(error)
        })

        await axios.get('usercrch/')
        .then(request=>{
            this.crchall=request.data

        })
        .catch(error=>
        {
            console.log(error)
        })

                await axios.get('profile')
        .then(request=>{  

            this.userprofile= request.data[0]
            this.profile_url= request.data[0].get_profile

            

        })
        .catch(error=>
        {
            console.log(error)
        })



        
        
        
        
    },
    methods:{
    showcomp(){
        this.activeTab = 'completed'
        this.shownchallenges= this.comchall

    

    },

    showcr(){
        this.activeTab = 'created'
        this.shownchallenges= this.crchall
        
    },

    getChallenge(chall){
        return chall.challenge ? chall.challenge : chall
    },

    getChallengeTitle(chall){
        return this.getChallenge(chall).Title
    },

    getChallengeCategory(chall){
        const challenge = this.getChallenge(chall)
        return challenge.Category ? challenge.Category.CategoryName : 'Challenge'
    },

    getChallengeInitial(chall){
        const title = this.getChallengeTitle(chall) || '?'
        return title.charAt(0).toUpperCase()
    },

    onFileChanged (event) {
        this.selectedFile = event.target.files[0]
    },
    async onUpload() {



        console.log(this.selectedFile)
        const formData = new FormData()
        formData.append('profile_pic', this.selectedFile)
        formData.append('user', this.user.id)



        try {
        
        let url= `updateprofile/${this.userprofile.id}`
        await axios.put(url, formData )
        .then(request=> {console.log(request)}).
        catch(error => {console.log(error)})
        
        }

        catch(err){
        await axios.post('createprofile', formData )
        .then(request=> {console.log(request)}).
        catch(error => {console.log(error)})
        }
        window.location.reload();
    },

    async onDelete(){
        console.log('here')
        let url= `updateprofile/${this.userprofile.id}`
        await axios.put(url, {"user": this.user.id, profile_pic: null})
        .then(request=> {console.log(request)}).
        catch(error => {console.log(error)})
        window.location.reload();

    },

    RouteToChall(chall){
        let path= ''
        if (chall.challenge){
            path= `/challenge/${chall.challenge.Category.slug}/${chall.challenge.slug}`
            
        }

        else {
            path= `/challenge/${chall.Category.slug}/${chall.slug}`
            
        }

        this.$router.push(path)
    }




    
    },


    


}
</script>

<style scoped>
.profile-card,
.challenge-panel {
  background: #ffffff;
  border: 1px solid rgba(21, 82, 99, 0.12);
  border-radius: 8px;
  box-shadow: 0 10px 24px rgba(21, 82, 99, 0.12);
  padding: 1.25rem;
}

.profile-card {
  margin-bottom: 1rem;
}

.profile-image {
  aspect-ratio: 1;
  border: 4px solid #ffc93c;
  border-radius: 50%;
  cursor: pointer;
  height: 150px;
  object-fit: cover;
  width: 150px;
}

.profile-label {
  color: #155263;
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0;
  text-transform: uppercase;
}

.profile-name {
  color: #2c3e50;
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 1rem;
}

.profile-stats {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
}

.stat-box {
  background: #f8fafb;
  border: 1px solid #e7ecef;
  border-radius: 8px;
  color: #6c757d;
  min-width: 130px;
  padding: 0.8rem 1rem;
}

.stat-box span {
  color: #155263;
  display: block;
  font-size: 1.5rem;
  font-weight: 800;
}

.challenge-panel-header {
  align-items: center;
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  justify-content: space-between;
  margin-bottom: 1rem;
}

.challenge-list {
  display: grid;
  gap: 0.7rem;
}

.challenge-row {
  align-items: center;
  background: #f8fafb;
  border: 1px solid #e7ecef;
  border-radius: 8px;
  color: #2c3e50;
  cursor: pointer;
  display: flex;
  gap: 0.85rem;
  padding: 0.85rem;
  text-align: left;
  transition: border-color 0.15s ease, transform 0.15s ease, background 0.15s ease;
  width: 100%;
}

.challenge-row:hover {
  background: #ffffff;
  border-color: #42b983;
  transform: translateY(-1px);
}

.challenge-icon {
  align-items: center;
  background: #155263;
  border-radius: 8px;
  color: #ffffff;
  display: flex;
  flex: 0 0 42px;
  font-weight: 800;
  height: 42px;
  justify-content: center;
  width: 42px;
}

.challenge-info {
  display: flex;
  flex: 1;
  flex-direction: column;
  min-width: 0;
}

.challenge-info strong,
.challenge-info small {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.challenge-info small {
  color: #6c757d;
}

.challenge-action {
  color: #155263;
  font-weight: 700;
}

.empty-state {
  background: #f8fafb;
  border-radius: 8px;
  color: #6c757d;
  padding: 1.5rem;
  text-align: center;
}

@media (max-width: 576px) {
  .challenge-panel-header {
    align-items: stretch;
  }

  .btn-group {
    width: 100%;
  }

  .btn-group .btn {
    flex: 1;
  }

  .challenge-action {
    display: none;
  }
}
</style>
