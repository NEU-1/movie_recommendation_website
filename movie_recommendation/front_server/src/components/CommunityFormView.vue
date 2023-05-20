<template>
    <div class="container">
      <div class="row">
        <router-link :to="{name: 'community' }">
          <button>뒤로가기</button>
        </router-link>
        </div>

        <div>
        <h2>게시글 작성</h2>
      </div>
      <br>
      <form @submit.prevent="createCommunity">
        <div>
          <input type="text" class="form-control" id="title" aria-describedby="titleHelp" v-model.trim="title" placeholder="제목">

        </div>
        <div class="mb-3 py-3">
          <textarea type="text" class="form-control" id="content" v-model.trim="content" placeholder="내용" style="height: 500px;"></textarea>
        </div>
        <button type="submit" class="btn btn-primary">등록</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  const API_URL = 'http://127.0.0.1:8000'
  
  export default {
    name: 'CommunityForm',
    data() {
      return {
        title: null,
        content: null,
      }
    },
    methods: {
      createCommunity() {
        const title = this.title
        const content = this.content
        if (!title) {
          alert('제목을 입력해주세요!')
          return
        } else if (!content) {
          alert('내용을 입력해주세요!')
          return
        }
        axios({
          method: 'post',
          url: `${API_URL}/api/v1/community/create/`,
          data: {
            title,
            content,
          },
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
          .then((res) => {
            // console.log(res.data)
            this.$router.push({ name: 'CommunityDetail', params: { community_pk: res.data.id }})
          })
          .catch(err => console.log(err))
      }
    }
  
  }
  </script>
  
  <style scoped>
  .container {
    max-width: 800px;
    margin: 0 auto;
  }
  </style>