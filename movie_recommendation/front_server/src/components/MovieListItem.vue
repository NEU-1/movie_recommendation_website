<template>
  <div>
    <h2>{{ movie.title }}</h2>
    <img :src="imageUrl" alt="Poster" />
    <p>{{ movie.overview }}</p>
  </div>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";

export default {
  computed: {
    ...mapGetters(["getMovieById"]),
    movie() {
      const movieId = this.$route.params.movieId;
      return this.getMovieById(movieId);
    },
    imageUrl() {
      const baseUrl = "https://image.tmdb.org/t/p/original";
      return baseUrl + this.movie.poster_path;
    },
  },
  methods: {
    fetchMovieDetails() {
      const movieId = this.$route.params.movieId;

      axios
        .get(`http://127.0.0.1:8000/api/v1/movies/list/${movieId}`)
        .then((response) => {
          const movieData = response.data[0];
          this.$store.commit("addMovie", movieData);
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

<style scoped></style>
