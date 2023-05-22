<template>
  <div>
    <h1>커뮤니티</h1>
    <div class="col-2" @click="goCreate">
    <button>추가</button></div>
    <ul>
      <li v-for="community in communities" :key="community.id">
        <div class="col-3">
          <p class="m-0 fw-bold fs-5 user" @click="goDetail(community)">{{ community.title }}</p>
        </div>
        <div class="col-2 text-center">
          <p class="m-0 fs-5 user" @click="goProfile(community)">{{ community.userName }}</p>
        </div>
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
    },
    goProfile(community) {
      this.$router.push({ name: 'Profile', params: { user_pk: this.community.user }})
    },
    goDetail(community) {
  this.$router.push({ name: 'CommunityDetail', params: { community_pk: community.id } })
    },
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