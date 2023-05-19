<template>
  <div class="movie-item">
    <div class="row">
      <MovieListItem
        v-for="(movie, i) in movies"
        :key="movie.id"
        :movie="movie"
        :movie_id="movie.movie_id"
        class="col-md-4"
      />
    </div>
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
  margin-bottom: 20px;
}

.movie-item .row {
  display: flex;
  flex-wrap: wrap;
  margin-right: -10px;
  margin-left: -10px;
}

.movie-item .col-md-4 {
  padding-right: 10px;
  padding-left: 10px;
  flex: 0 0 33.33%;
  max-width: 33.33%;
}

.movie-item img {
  max-width: 100%;
  height: auto;
  border-radius: 4px;
  margin-bottom: 10px;
}

.movie-item h3 {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 5px;
}

.movie-item p {
  font-size: 14px;
  color: #6c757d;
}
</style>
