<template>
  <div>
    <h2>Movie List</h2>
    <div class="movie-list">
      <MovieListItem v-for="movie in movies" :key="movie.id" :movie="movie" />
    </div>
  </div>
</template>

<script>
import MovieListItem from './MovieListItem.vue';
import moviesData from './movies.json';

export default {
  components: {
    MovieListItem
  },
  data() {
    return {
      movies: moviesData
    };
  }
};
</script>

<style scoped>
.movie-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
}
</style>