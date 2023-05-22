<template>
  <div class="container my-profile">
    <div class="row justify-content-center">
      <div class="col-sm-9 col-12">
        <div class="user-heading text-center pb-4">
          <h1>{{ user?.username }}</h1>
        </div>
        <div class="user-details d-flex justify-content-around">
          <div class="follow-info" @click="openModal(1)">
            <h2>
              <strong>{{ followersLength }}</strong>
            </h2>
            <p>팔로워</p>
          </div>
          <div class="follow-info" @click="openModal(2)">
            <h2>
              <strong>{{ followingsLength }}</strong>
            </h2>
            <p>팔로잉</p>
          </div>
          <div class="follow-info">
            <h2>
              <strong>{{ user.like_movies?.length }}</strong>
            </h2>
            <p>좋아요한 영화 수</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.my-profile {
  padding: 2rem 0;
  background-color: #f8f9fa;
  border-radius: 5px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}

.user-heading h1 {
  font-size: 2.5rem;
  color: #343a40;
}

.user-details {
  margin-top: 2rem;
}

.follow-info {
  background-color: white;
  padding: 1.5rem;
  border-radius: 5px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}

.follow-info h2 {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
}

.follow-info p {
  color: #6c757d;
}
</style>

<script>
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "MyProfile",
  data() {
    return {
      me: [],
      user: [],
      show1: false,
      show2: false,
    };
  },
  created() {
    this.getMyProfile();
  },
  methods: {
    async getMyProfile() {
      if (this.$store.getters.isLogin === false) {
        return;
      }
      try {
        const me = await this.fetchProfile();
        const user = await this.fetchName(me.pk);
        this.me = me;
        this.user = user;
      } catch (err) {
        console.error(err);
      }
    },
    fetchProfile() {
      return axios({
        method: "get",
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${this.$store.state.token.key}`,
        },
      }).then((res) => res.data);
    },
    fetchName(my_pk) {
      return axios({
        method: "get",
        url: `${API_URL}/userinfo/user/${my_pk}/`,
      }).then((res) => res.data);
    },
    openModal(modalNumber) {
      if (modalNumber === 1) {
        this.show1 = true;
      } else {
        this.show2 = true;
      }
    },
    closeModal(modalNumber) {
      if (modalNumber === 1) {
        this.show1 = false;
      } else {
        this.show2 = false;
      }
    },
  },
  computed: {
    followingsLength() {
      return this.user.followings?.length || 0;
    },
    followersLength() {
      return this.user.followers?.length || 0;
    },
  },
};
</script>
