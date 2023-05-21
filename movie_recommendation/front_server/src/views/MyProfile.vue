<template>
  <div class="container my-profile">
    <div class="row">
      <div class="col-sm-9 col-12">
        <div class="col-12 d-flex justify-content-around pb-2">
          <h1>{{ user?.username }}</h1>
        </div>
        <div class="col-sm-12 divider text-center row d-flex justify-content-around" style="margin-bottom:20px">
            <div class="col-sm-3 col-12 follow-info" @click="openModal(1)">
              <h2><strong>{{ followersLength }}</strong></h2>                    
              <p><small>팔로워</small></p>
            </div>
            <div class="col-sm-3 col-12 follow-info" @click="openModal(2)">
              <h2><strong>{{ followingsLength }}</strong></h2>                    
              <p><small>팔로잉</small></p>
            </div>
            <div class="col-sm-3 col-12">
              <h2><strong>{{ user.like_movies?.length }}</strong></h2>                    
              <p><small>좋아요한 영화 수</small></p>
            </div>
        </div>            
      </div>
    </div>
    <br>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: "MyProfile",
  data() {
    return {
      me: [],
      user: [],
      show1: false,
      show2: false,
    }
  },
  created() {
    this.getMyProfile()
  },
  methods: {
    async getMyProfile() {
      if (this.$store.getters.isLogin === false) {
        return
      }
      try {
        const me = await this.fetchProfile()
        const user = await this.fetchName(me.pk)
        this.me = me
        this.user = user
      } catch (err) {
        console.error(err)
      }
    },
    fetchProfile() {
      return axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      }).then(res => res.data)
    },
    fetchName(my_pk) {
      return axios({
        method: 'get',
        url: `${API_URL}/userinfo/user/${my_pk}/`,
      }).then(res => res.data)
    },
    openModal(modalNumber) {
      if (modalNumber === 1) {
        this.show1 = true
      } else {
        this.show2 = true
      }
    },
    closeModal(modalNumber) {
      if (modalNumber === 1) {
        this.show1 = false
      } else {
        this.show2 = false
      }
    },
  },
  computed: {
    followingsLength() {
      return this.user.followings?.length || 0
    },
    followersLength() {
      return this.user.followers?.length || 0
    },
  },
}
</script>