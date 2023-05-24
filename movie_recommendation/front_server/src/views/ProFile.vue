<template>
  <div class="proFile">
    <div class="user-heading text-center pb-4">
      <h1>{{ user?.username }} 의 프로필</h1>
    </div>
    <button v-if="me && me.id !== user.id" @click="followUser" class="btn btn-primary">
      팔로우
    </button>
    <div class="user-details d-flex justify-content-around flex-wrap">
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
      <div class="follow-info" v-if="user && user.like_movies">
        <h2>
          <strong>{{ user.like_movies.length }}</strong>
        </h2>
        <p>좋아요한 영화 수</p>
      </div>
    </div>
    <h3 class="white-text">좋아요한 영화</h3>
    <div class="movie-grid">
      <div class="movie-item" v-for="movie in movieList" :key="movie.id">
        <router-link :to="`/movies/${movie.id}`">
          <img :src="imageUrl(movie)" alt="Poster" />
          <h3>{{ movie.title }}</h3>
        </router-link>
      </div>

    </div>
  </div>
</template>

<style scoped>
.proFile {
  padding: 2rem 0;
  background-color: rgb(83, 131, 234);
  width: 800px;
}

.movie-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.movie-item {
  flex: 1 0 200px;
  margin: 1rem;
}

.img {
  width: 50px;
}

.user-heading h1 {
  font-size: 3rem;
  color: #343a40;
}

.user-details {
  margin-top: 3rem;
}

.white-text {
  color: white;
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

img {
  width: 200px;
  height: 300px;
  object-fit: cover;
  /* 유지하면서 이미지 비율이 유지되도록 이미지를 조정합니다. */
}
</style>

<script>
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";
const MOVIE_API_URL = "http://127.0.0.1:8000/api/v1/movies/";
const IMAGE_URL = "https://image.tmdb.org/t/p/original";

export default {
  name: "ProFile",
  data() {
    return {
      me: null,
      user: null,
      show1: false,
      show2: false,
      movie: {},
      movieList: [],
    };
  },
  async created() {
    await this.getMyProfile();
    await this.getProfile();
    await this.getMovies();
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
          console.log("프로필 정보를 받아오지 못했습니다.");
          return;
        }
        const user = await this.fetchName(me.pk);
        if (!user) {
          console.log("사용자 정보를 받아오지 못했습니다.");
          return;
        }
        this.me = me;
        this.user = user;
      } catch (err) {
        console.error(err);
      }
    },
    async getProfile() {
      const userId = this.$route.params.user_pk;
      if (!userId) {
        console.log("사용자 ID가 없습니다.");
        this.user = null;
        return;
      }

      try {
        const user = await this.fetchProfile(userId);
        if (!user) {
          console.log("사용자 정보를 받아오지 못했습니다.");
          return;
        }

        this.user = user;
      } catch (err) {
        console.error(err);
      }
    },
    async fetchProfile(user_pk) {
      const tokenKey = this.$store.state.token;
      const url = user_pk
        ? `${API_URL}/user/profile/${user_pk}/`
        : `${API_URL}/accounts/user/`;
      try {
        const res = await axios.get(url, {
          headers: {
            Authorization: `Token ${tokenKey}`,
          },
        });
        return res.data;
      } catch (err) {
        console.log("프로필 자격 인증 데이터가 없습니다.");
        return null;
      }
    },
    async fetchName(my_pk) {
      if (!my_pk) {
        console.log("사용자 PK가 없습니다.");
        return null;
      }

      try {
        const res = await axios.get(`${API_URL}/user/profile/${my_pk}/`);
        return res.data;
      } catch (err) {
        console.log("네임 자격 인증 데이터가 없습니다.");
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
      if (this.me.pk === this.user.id) {
        alert("자신을 팔로우할 수 없습니다.");
        return;
      }
      axios({
        url: `${API_URL}/user/follow/${this.me.pk}/${this.user.id}/`,
        headers: { Authorization: `Token ${this.$store.state.token}` },
        method: "POST",
      })
        .then((res) => {
          if (res.data) {
            alert("팔로우가 완료되었습니다.");
          }
        })
        .catch((err) => {
          console.error(err);
        });
    },
    async getMovies() {
      this.movieList = [];
      for (const movieId of this.user.like_movies) {
        try {
          const response = await axios.get(`${MOVIE_API_URL}${movieId}`);
          this.movieList.push(response.data);
        } catch (err) {
          console.error(err);
        }
      }
    },
    imageUrl(movie) {
      const baseUrl = "https://image.tmdb.org/t/p/original/";
      return baseUrl + movie.poster_path;
    },
  },
  computed: {
    followingsLength() {
      return this.user ? this.user.followings?.length || 0 : 0;
    },
    followersLength() {
      return this.user ? this.user.followers?.length || 0 : 0;
    },
  },
};
</script>
