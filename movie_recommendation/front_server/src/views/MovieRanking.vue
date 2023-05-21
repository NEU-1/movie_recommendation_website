<template>
  <div>
    <nav>
      <ul class="no-bullet">
        <li v-for="genre in genres" :key="genre.pk" @click="filterByGenre(genre.pk)">
          {{ genre.fields.name }}
        </li>
      </ul>
    </nav>
    <ul class="no-bullet">
      <li v-for="movie in sortedMovies" :key="movie.id">
        <h2>{{ movie.fields.title }}</h2>
        <p>Rating: {{ movie.fields.vote_average }}</p>
      </li>
    </ul>
  </div>
</template>

<style>
.no-bullet {
  list-style: none;
  padding-left: 0;
}
</style>


<script>
import axios from "axios";

export default {
  data() {
    return {
      movies: [],
      genres: [],
      selectedGenre: null,
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
          .filter((movie) => movie.fields.genres.includes(this.selectedGenre))
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
        .get("http://127.0.0.1:8000/api/v1/movies/genre/")
        .then((response) => {
          this.genres = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    filterByGenre(genreId) {
      this.selectedGenre = genreId;
    },
  },
};
</script>


<style>
.no-bullet {
  list-style: none;
  padding-left: 0;
}
</style>