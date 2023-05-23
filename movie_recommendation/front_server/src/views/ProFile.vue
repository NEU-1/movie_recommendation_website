<template>
  <div class="proFile">
    <div class="user-heading text-center pb-4">
      <h1>{{ user?.username }} 의 프로필 정보</h1>
      <!-- ({{ me?.username }}) -->
    </div>
    <div class="user-details d-flex justify-content-around flex-wrap">
      <div class="follow-info" @click="openModal(1)">
        <h2>
          <!-- <strong>{{ followersLength }}</strong> -->
        </h2>
        <p>팔로워</p>
      </div>
      <div class="follow-info" @click="openModal(2)">
        <h2>
          <!-- <strong>{{ followingsLength }}</strong> -->
        </h2>
        <p>팔로잉</p>
      </div>
      <div class="follow-info">
        <h2>
          <!-- <strong>{{ user.like_movies?.length }}</strong> -->
        </h2>
        <p>좋아요한 영화 수</p>
      </div>
    </div>
    <!-- <div class="follow-button" v-if="me.id !== user.id"> -->
    <button @click="followUser">팔로우</button>
  </div>
</template>

<style scoped>
.proFile {
  padding: 2rem 0;
  background-color: rgb(83, 131, 234);
}

.user-heading h1 {
  font-size: 3rem;
  color: #343a40;
}

.user-details {
  margin-top: 3rem;
}

.follow-info {
  background-color: white;
  padding: 2rem;
  border-radius: 5px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
  flex: 1 0 200px;
  margin: 1rem;
  text-align: center;
}

.follow-info h2 {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.follow-info p {
  color: #6c757d;
  font-size: 1.2rem;
}
</style>
.my-profile {
  padding: 2rem 0;
  background-color: #f8f9fa;
  border-radius: 5px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}

.user-heading h1 {
  font-size: 3rem;
  color: #343a40;
}

.user-details {
  margin-top: 3rem;
}

.follow-info {
  background-color: white;
  padding: 2rem;
  border-radius: 5px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
  flex: 1 0 200px;
  margin: 1rem;
  text-align: center;
}

.follow-info h2 {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.follow-info p {
  color: #6c757d;
  font-size: 1.2rem;
}
</style>

<script>
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "ProFile",
  data() {
    return {
      me: null,
      user: null,
      show1: false,
      show2: false,
    };
  },
  created() {
    this.getMyProfile();
  },
  methods: {
    async getMyProfile() {
      if (!this.$store.getters.isLogin) {
        this.me = null;
        this.user = null;
        return;
      }

      try {
        const me = await this.fetchProfile();
        if (!me) {
          console.log('프로필 정보를 받아오지 못했습니다.');
          return;
        }
        const user = await this.fetchName(me.pk);
        if (!user) {
          console.log('사용자 정보를 받아오지 못했습니다.');
          return;
        }
        this.me = me;
        this.user = user;
      } catch (err) {
        console.error(err);
      }
    },
    async fetchProfile() {
      const tokenKey = this.$store.state.token;
      console.log('Authorization Token Key:', tokenKey);

      try {
        const res = await axios.get(`${API_URL}/accounts/user/`, {
          headers: {
            Authorization: `Token ${tokenKey}`,
          },
        });
        return res.data;
      } catch (err) {
        console.log('프로필 자격 인증 데이터가 없습니다.');
        return null;
      }
    },
    async fetchName(my_pk) {
      if (!my_pk) {
        console.log('사용자 PK가 없습니다.');
        return null;
      }

      try {
        const res = await axios.get(`${API_URL}/user/profile/${my_pk}/`);
        return res.data;
      } catch (err) {
        console.log('네임 자격 인증 데이터가 없습니다.');
        return null;
      }
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
    followUser() {
      axios
        .post(
          `${API_URL}/user/follow/${this.me.id}/${this.user.id}`,
          null,
          {
            headers: { Authorization: `Token ${this.$store.state.token}` },
          }
        )
        .then((res) => {
          if (res.data) {
            alert('팔로우가 완료되었습니다.');
            this.getMyProfile();
          }
        })
        .catch((err) => {
          console.error(err);
        });
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


