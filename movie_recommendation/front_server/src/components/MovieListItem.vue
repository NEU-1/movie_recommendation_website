<template>
  <div class="movie-item">
    <div
      class="poster-container"
      @mouseover="showDetailsButton = true"
      @mouseleave="showDetailsButton = false"
    >
      <img :src="imageUrl" alt="Poster" class="poster-image" />
      <router-link
        v-if="showDetailsButton"
        class="details-button"
        :to="`/movie/${movie.id}`"
      >
        상세보기
      </router-link>
    </div>
    <h2 class="movie-title">{{ movie.title }}</h2>
  </div>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";

export default {
  data() {
    return {
      movie: {},
      showDetailsButton: false,
    };
  },
  mounted() {
    // 영화 세부 내용을 조회하는 메서드를 호출합니다.
    this.fetchMovieDetails();
  },
  methods: {
    fetchMovieDetails() {
      const movieId = this.$route.params.movieId;

      axios
        .get(`http://127.0.0.1:8000/api/v1/movies/list/${movieId}`)
        .then((response) => {
          const movieData = response.data[0]; // 응답이 단일 영화 객체를 포함하는 배열이라고 가정합니다.
          this.movie = {
            id: movieData.id,
            title: movieData.fields.title,
            description: movieData.fields.overview,
            // 표시할 다른 영화 세부 정보를 추가하세요
          };
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    if (!this.getMovieById(this.$route.params.movieId)) {
      this.fetchMovieDetails();
    }
  },
};
</script>

<style scoped>
.movie-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
}

.poster-container {
  position: relative;
  text-align: center;
}

.poster-image {
  width: 360px;
  height: auto;
}

.details-button {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 10px 20px;
  font-size: 16px;
  font-weight: bold;
  color: white;
  background-color: #000;
  border: none;
  border-radius: 4px;
  opacity: 0.8;
  cursor: pointer;
}

.movie-title {
  font-weight: bold;
  color: white;
  margin-top: 10px;
}
</style>
