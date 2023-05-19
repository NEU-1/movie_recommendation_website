<template>
  <div class="movie-detail">
    <h2>{{ movie.title }}</h2>
    <img :src="imageUrl" alt="Poster" />
    <p>{{ movie.overview }}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      movie: {},
    };
  },
  async created() {
    const movie_id = this.$route.params.movie_id;

    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/api/v1/movies/${movie_id}/`
      );
      this.movie = response.data;
      console.log(this.movie);
    } catch (error) {
      console.error(error);
    }

  },
  computed: {
    imageUrl() {
      const baseUrl = "https://image.tmdb.org/t/p/original/";
      return baseUrl + this.movie.poster_path;
    },
  },
};
</script>

<style scoped>
/* 여기에 스타일을 추가하십시오 */
</style>