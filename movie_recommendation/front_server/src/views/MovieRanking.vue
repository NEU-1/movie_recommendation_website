<template>
  <div>
    <nav>
      <ul>
        <li v-for="genre in genres" :key="genre.id" @click="filterByGenre(genre.id)">
          {{ genre.name }}
        </li>
      </ul>
    </nav>
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
      genres: [],  
      selectedGenre: null,  // 선택한 장르를 저장할 변수 추가
    };
  },
  mounted() {
    this.fetchMovies();
    this.fetchGenres();  
  },
  computed: {
    sortedMovies() {
      if (this.selectedGenre === null) {
        return this.movies.sort(
          (a, b) => b.fields.vote_average - a.fields.vote_average
        );
      } else {
        return this.movies
          .filter((movie) => movie.fields.genre_ids.includes(this.selectedGenre))  // 선택한 장르에 맞게 필터링
          .sort((a, b) => b.fields.vote_average - a.fields.vote_average);
      }
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
    fetchGenres() {  
      axios
        .get("http://127.0.0.1:8000/api/v1/genres/your-url/")
        .then((response) => {
          this.genres = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    filterByGenre(genreId) {  // 장르별 필터링을 위한 메서드 추가
      this.selectedGenre = genreId;
    },
  },
};
</script>
