<template>
  <div class="container">
    <img
      :src="require(`../assets/펭구2.png`)"
      alt="Side image"
      class="side-image left-image"
    />
    <img
      :src="require(`../assets/펭구1.png`)"
      alt="Side image"
      class="side-image right-image"
    />
    <nav class="genre-nav">
      <ul class="no-bullet">
        <h1><b>MV.GG RANKING</b></h1>
        <BR />
        <li
          class="genre-item"
          v-for="genre in genres"
          :key="genre.id"
          @click="filterByGenre(genre.pk)"
          :class="{ 'genre-selected': selectedGenre === genre.pk }"
        >
          {{ genre.fields.name }}
        </li>
      </ul>
    </nav>
    <ul class="no-bullet movie-list">
      <li
        class="movie-item"
        v-for="(movie, index) in sortedMovies"
        :key="movie.id"
      >
        <img
          v-if="index < 5"
          :src="require(`../assets/다이아.png`)"
          alt="Movie image"
          class="movie-img"
        />
        <img
          v-if="index >= 5 && index < 10"
          :src="require(`../assets/플레티넘.png`)"
          alt="Movie image"
          class="movie-img"
        />
        <img
          v-if="index >= 10"
          :src="require(`../assets/골드.png`)"
          alt="Movie image"
          class="movie-img"
        />

        <div class="movie-rank">{{ index + 1 }}</div>
        <div class="movie-info">
          <router-link :to="`/movies/${movie.pk}`">
            <h2 class="movie-title">{{ movie.fields.title }}</h2>
          </router-link>
          <p class="movie-rating">Rating: {{ movie.fields.vote_average }}</p>
        </div>
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
      selectedGenre: null,
    };
  },
  mounted() {
    this.fetchMovies();
    this.fetchGenres();
  },
  computed: {
    sortedMovies() {
      let uniqueMovies = [];
      let movieMap = new Map();

      for (const movie of this.movies) {
        if (!movieMap.has(movie.pk)) {
          movieMap.set(movie.pk, true); // set any value to Map
          uniqueMovies.push(movie);
        }
      }

      uniqueMovies = uniqueMovies.filter(
        (movie) => movie.fields.vote_average !== 10
      );

      if (this.selectedGenre === null) {
        return uniqueMovies.sort(
          (a, b) => b.fields.vote_average - a.fields.vote_average
        );
      } else {
        return uniqueMovies
          .filter((movie) => movie.fields.genres.includes(this.selectedGenre))
          .sort((a, b) => b.fields.vote_average - a.fields.vote_average);
      }
    },
  },

  methods: {
    fetchMovies() {
      axios
        .get("http://127.0.0.1:8000/api/v1/movies/")
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

<style scoped>
.container {
  font-family: Arial, sans-serif;
  color: #333;
  max-width: 1000px;
  margin: 0 auto;
}
.left-image {
  margin-right: 200px;
}

.genre-nav {
  background-color: #f8f9fa;
  padding: 1em;
  border-radius: 5px;
  margin-bottom: 2em;
}

.genre-item {
  display: inline-block;
  margin-right: 2em;
  margin-bottom: 1em; /* Add vertical space between buttons */
  padding: 0.5em 1em;
  background-color: #007bff;
  color: white;
  border-radius: 3px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.genre-item:hover,
.genre-selected {
  background-color: black;
}

.movie-list {
  display: grid;
  grid-template-columns: 1fr; /* Show only one movie per row */
  gap: 1em;
}

.movie-item {
  padding: 1em;
  background-color: #f8f9fa;
  border-radius: 5px;
  transition: transform 0.3s;
  display: flex; /* Add this */
  align-items: center; /* Add this */
}

.movie-img {
  width: 50px;
  height: 50px;
  margin-right: 10px;
}

.movie-item:hover {
  transform: scale(1.02);
}

.movie-rank {
  font-size: 1.5em;
  color: grey;
  margin-right: 0.5em;
}

.movie-title {
  margin: 0 0 0.5em;
  font-size: 1.5em; /* Increase font size */
  color: #007bff;
}

.movie-rating {
  margin: 0;
  color: #6c757d;
  font-weight: bold;
}

.movie-info {
  flex-grow: 1; /* Add this */
}

.no-bullet {
  list-style: none;
  padding-left: 0;
}
</style>
