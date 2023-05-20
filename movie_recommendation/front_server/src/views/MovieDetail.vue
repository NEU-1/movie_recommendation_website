<template>
  <div class="movie-detail">
    <h2>{{ movie.data.title }}</h2>
    <img :src="imageUrl" alt="Poster" />
    <p>{{ movie.data.overview }}</p>
    <p>{{ formattedGenres }}</p>
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
    const movie_id = this.$route.params.id;
    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/api/v1/movies/${movie_id}/`
      );
      this.movie = response.data;
    } catch (error) {
      console.error(error);
    }
  },
  computed: {
    imageUrl() {
      const baseUrl = "https://image.tmdb.org/t/p/original/";
      return baseUrl + this.movie.data.poster_path;
    },
    formattedGenres() {
      if (this.movie.data.genres && Array.isArray(this.movie.data.genres)) {
        return this.movie.data.genres.map(genre => genre.name).join(", ");
      }
      return "";
    }
  },
};
</script>

<style scoped>
/* 여기에 스타일을 추가하십시오 */
</style>
