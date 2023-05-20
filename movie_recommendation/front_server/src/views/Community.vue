<template>
  <div>
    <h1>커뮤니티</h1>
    <div class="col-2" @click="goCreate">
    <button>추가</button></div>
    <ul>
      <li v-for="community in communities" :key="community.id">
        <p>작성자: {{ community.user }}</p>
        <h2>{{ community.title }}</h2>
        <p>{{ community.content }}</p>
        
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name:'CommunityView',
  data() {
    return {
      isLogin: this.$store.getters.isLogin,
    }
  },
  computed: {
    communities() {
      return this.$store.state.communities
    }
  },
  methods: {
    getCommunityList() {
      this.$store.dispatch('getCommunityList')
    },
    goCreate() {
      if (this.isLogin === false) {
        alert('게시글을 작성하시려면 로그인을 하세요!')
        return
      }
      this.$router.push({ name: 'CommunityCreate' })
    }
  },
  created() {
    this.getCommunityList()
  }
}
</script>

<style>
.community {
  padding-bottom: 450px;
}
</style>