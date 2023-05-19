<template>
  <div>
    <h2>Movie</h2>
    <div class="movie-list">
      <MovieList :movies="movies" />
    </div>
  </div>
</template>

<script>
import MovieList from "@/components/MovieList.vue";
import axios from "axios";

export default {
  name: "MovieView",

  components: {
    MovieList,
  },
  data() {
    return {
      movies: [],
    };
  },
  async created() {
    try {
      const response = await axios.get(
        "http://127.0.0.1:8000/api/v1/movies/list/"
      );
      this.movies = response.data;
    } catch (error) {
      console.error(error);
    }
  },
};
</script>

<style scoped>
.movie-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
}
</style>
