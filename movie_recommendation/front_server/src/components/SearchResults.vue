<template>
  <div class="search-results">
    <div v-if="movies.length === 0">
      <img src="../assets/동석.png" alt="No results" class="no-results-image" />
      <br>
      <div class="no-results-message">검색 결과가 없습니다.</div>
    </div>
    <div v-else>
      <div v-for="movie in movies" :key="movie.id" class="movie-item">
        <router-link :to="`/movies/${movie.id}`">
          <div class="movie-poster">
            <img :src="getMoviePoster(movie)" :alt="movie.title" />
          </div>
          <div class="movie-title">{{ movie.title }}</div>
        </router-link>
      </div>
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
        const response = await axios.get(`http://127.0.0.1:8000/api/v1/movies/search/?q=${q}`);
        this.movies = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    getMoviePoster(movie) {
      const baseUrl = 'https://image.tmdb.org/t/p/original/';
      return baseUrl + movie.poster_path;
    },
  },
};
</script>

<style scoped>
.search-results {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.movie-item {
  width: 200px;
  margin: 20px;
}

.movie-poster img {
  width: 200px;
  height: 300px;
}

.movie-title {
  text-align: center;
  color: white;
  margin-top: 10px;
}

.no-results-image {
  width: 350px;
  height: 350px;
  margin: 0 auto;
}

.no-results-message {
  text-align: center;
  color: white;
  margin-top: 10px;
  font-size: 24px;
  font-weight: bold;
}
</style>