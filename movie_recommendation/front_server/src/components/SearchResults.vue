<template>
    <div class="search-results">
      <div v-for="movie in movies" :key="movie.movie_id">
        <router-link :to="`/movies/${movie.movie_id}`">{{ movie.title }}</router-link>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        movies: [],
      };
    },
    async created() {
      await this.fetchMovies();
    },
    watch: {
      '$route.query.q': {
        immediate: true,
        handler: 'fetchMovies',
      },
    },
    methods: {
      async fetchMovies() {
        const q = this.$route.query.q;
        try {
          const response = await axios.get(`http://127.0.0.1:8000/api/v1/movies/search/?q=${q}`)
          this.movies = response.data;
        } catch (error) {
          console.error(error);
        }
      },
    },
  };
  </script>