<template>
  <div>
    <h2>Movie List</h2>
    <div class="movie-list">
      <p>영화탭입니다</p>
      <MovieListItem
        v-for="movie in movies.data"
        :key="movie.id"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import MovieList from "@/components/MovieList.vue";

export default {
  name: "MovieView",

  components: {
    MovieList,
  },
  data() {
    return {
      movies: [],
    };
  },
  async created() {
    const response = await axios.get(
      "http://127.0.0.1:8000/api/v1/movies/your-url/"
    );
    this.movies = response.data;
  },
  created() {
    this.getMovies();
  },
  methods: {
    getMovies() {
      this.$store.dispatch("getMovies");
    },
  },
};
</script>

<style scoped>
.movie-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
}
</style>
