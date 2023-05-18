<template>
  <div>
    <h2>Movie List</h2>
    <div class="movie-list">
      <MovieListItem v-for="movie in movies" :key="movie.id" :movie="movie" />
    </div>
  </div>
</template>

<script>
import MovieListItem from "@/components/MovieListItem.vue";
import moviesData from "@/views/movies.json";

export default {
  name: "MovieListView",

  components: {
    MovieListItem,
  },
  data() {
    return {
      movies: moviesData,
    };
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
