<template>
  <div class="movie-item">
    <MovieListItem
      v-for="movie in movies"
      :key="movie.pk"
      :movie="movie.fields"
    />
  </div>
</template>

<script>
import MovieListItem from "@/components/MovieListItem";

export default {
  name: "MovieList",

  components: {
    MovieListItem,
  },

  props: {
    movies: {
      type: Array,
      required: true,
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
