<template>
  <div>
    <h1>Movie Ranking</h1>
    <ul>
      <li v-for="movie in sortedMovies" :key="movie.id">
        <h2>{{ movie.fields.title }}</h2>
        <p>Rating: {{ movie.fields.vote_average }}</p>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      movies: [],
    };
  },
  mounted() {
    this.fetchMovies();
  },
  computed: {
    sortedMovies() {
      return this.movies.sort(
        (a, b) => b.fields.vote_average - a.fields.vote_average
      );
    },
  },
  methods: {
    fetchMovies() {
      axios
        .get("http://127.0.0.1:8000/api/v1/movies/your-url/")
        .then((response) => {
          this.movies = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>
