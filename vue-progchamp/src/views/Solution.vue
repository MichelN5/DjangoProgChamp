<template>
<div class="container my-4 solution-page">
  <div class="page-panel">
    <div class="d-flex flex-wrap justify-content-between align-items-start gap-2 mb-3">
      <div>
        <p class="section-kicker mb-1">{{ challenge.Category ? challenge.Category.CategoryName : 'Challenge' }}</p>
        <h2 class="mb-0">{{ challenge.Title || 'Solution' }}</h2>
      </div>
      <button type="button" class="btn btn-outline-secondary btn-sm" @click="goBack">
        Back to challenge
      </button>
    </div>

    <section class="solution-card mb-4">
      <div class="d-flex justify-content-between align-items-center mb-2">
        <h5 class="mb-0">Official Solution</h5>
        <span class="badge bg-success">Solved</span>
      </div>
      <pre class="solution-code mb-0"><code>{{ challenge.Solution }}</code></pre>
    </section>

    <section class="comments-card">
      <div class="d-flex justify-content-between align-items-center mb-3">
        <div>
          <h5 class="mb-0">Comments</h5>
          <small class="text-muted">{{ comments.length }} {{ comments.length === 1 ? 'comment' : 'comments' }}</small>
        </div>
      </div>

      <div class="comment-form mb-3">
        <textarea v-model="commenttext" class="form-control" rows="3" placeholder="Add your comment"></textarea>
        <div class="d-flex justify-content-end mt-2">
          <button type="button" class="btn btn-success" :disabled="!commenttext.trim()" @click="pubcomment">
            Comment
          </button>
        </div>
      </div>

      <div v-if="!comments.length" class="empty-state">
        No comments yet.
      </div>

      <div v-for="comment in comments" :key="comment.id" class="comment-item">
        <div class="comment-avatar">
          {{ getInitial(getCommentUsername(comment)) }}
        </div>
        <div class="comment-body">
          <div class="comment-author">{{ getCommentUsername(comment) }}</div>
          <p class="mb-0">{{ comment.Comment }}</p>
        </div>
      </div>
    </section>
  </div>
</div>
</template>

<script>

import axios from 'axios'
export default {
    data(){
        return {
            challenge: '',
            comments: [],
            commenttext: '',
            user: [],
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

      await axios.get(`comments/${this.challenge.id}/`)
      .then(request=>{
        this.comments=request.data
      })
      .catch(error =>{
        console.log(error)
      })

      await axios.get('getuser')
      .then(request=>{this.user = request.data[0]})



    },

    methods: {
      getInitial(username){
        return username ? username.charAt(0).toUpperCase() : '?'
      },
      getCommentUsername(comment){
        if (comment.User && comment.User.username) {
          return comment.User.username
        }

        return this.user.username || 'User'
      },
      goBack(){
        const category_slug = this.$route.params.category_slug
        const product_slug = this.$route.params.product_slug
        this.$router.push(`/challenge/${category_slug}/${product_slug}`)
      },
      async pubcomment(){
        if (!this.commenttext.trim()) {
          return
        }
        let data =         {
          "Comment": this.commenttext,
          "User": this.user.id,
          "Challenge": this.challenge.id

        }

        console.log(data)



        await axios.post('comments/create', data)
        .then(request=>
        {console.log(request);
        this.commenttext = ''
        this.comments.unshift({
          ...request.data,
          User: this.user,
        })})

      }
    }
    
}
</script>

<style scoped>
.page-panel {
  background: #ffffff;
  border: 1px solid rgba(21, 82, 99, 0.12);
  border-radius: 8px;
  box-shadow: 0 10px 24px rgba(21, 82, 99, 0.12);
  padding: 1.25rem;
}

.section-kicker {
  color: #155263;
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0;
  text-transform: uppercase;
}

.solution-card,
.comments-card {
  border: 1px solid #e7ecef;
  border-radius: 8px;
  padding: 1rem;
}

.solution-code {
  background: #182f3a;
  border-radius: 6px;
  color: #f8f9fa;
  font-size: 0.95rem;
  line-height: 1.55;
  max-height: 460px;
  overflow: auto;
  padding: 1rem;
  text-align: left;
  white-space: pre-wrap;
}

.comment-form {
  background: #f8fafb;
  border: 1px solid #e7ecef;
  border-radius: 8px;
  padding: 0.85rem;
}

.comment-item {
  align-items: flex-start;
  border-top: 1px solid #edf0f2;
  display: flex;
  gap: 0.75rem;
  padding: 0.9rem 0;
  text-align: left;
}

.comment-item:first-of-type {
  border-top: 0;
}

.comment-avatar {
  align-items: center;
  background: #155263;
  border-radius: 50%;
  color: #ffffff;
  display: flex;
  flex: 0 0 38px;
  font-weight: 700;
  height: 38px;
  justify-content: center;
  width: 38px;
}

.comment-body {
  min-width: 0;
}

.comment-author {
  color: #155263;
  font-weight: 700;
}

.empty-state {
  background: #f8fafb;
  border-radius: 8px;
  color: #6c757d;
  padding: 1rem;
  text-align: center;
}
</style>
