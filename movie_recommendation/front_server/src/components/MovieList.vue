<template>
  <div class="movie-item">
    <MovieListItem v-for="movie in movies" :key="movie.id" :movie="movie" />
    <p>리스트입니다</p>
  </div>
</template>

<script>
import MovieListItem from "@/components/MovieListItem";

export default {
  name: "movieList",

  components: {
    MovieListItem,
  },

  props: {
    movies: {
      type: Object,
      required: true,
    },
  },

  computed: {
    movies() {
      return rhis.$store.state.movies;
    },
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

.movie-item img {
  width: 200px;
  height: auto;
}
</style>
