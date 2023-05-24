<template>
  <div class="movie-item">
    <div class="row">
      <MovieListItem
        v-for="movie in paginatedMovies"
        :key="movie.id"
        :movie="movie"
        :movie_id="movie.pk"
        class="col-md-4"
      />
    </div>
    <div class="pagination">
      <button
        class="btn btn-primary btn-lg arrow-btn"
        v-if="currentPage > 1"
        @click="currentPage--"
      >
        &larr; Previous
      </button>
      <button
        class="btn btn-primary btn-lg arrow-btn"
        v-if="currentPage < pageCount"
        @click="currentPage++"
      >
        Next &rarr;
      </button>
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

  data() {
    return {
      currentPage: 1,
      pageSize: 3,
    };
  },

  props: {
    movies: {
      type: Array,
      required: true,
    },
  },

  computed: {
    pageCount() {
      return Math.ceil(this.movies.length / this.pageSize);
    },

    paginatedMovies() {
      const start = (this.currentPage - 1) * this.pageSize;
      const end = start + this.pageSize;
      return this.movies.slice(start, end);
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
.pagination {
  display: flex;
  justify-content: space-between;
  margin: 20px 0;
}

.arrow-btn {
  cursor: pointer;
  margin: 0 5px;
}
</style>
