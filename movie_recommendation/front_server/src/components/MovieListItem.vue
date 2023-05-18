<template>
  <div>
    <h2>{{ movie.title }}</h2>
    <img :src="imageUrl" alt="Poster" />
    <p>{{ movie.overview }}</p>
  </div>
</template>

<script>
export default {
  name: "MovieListItem",

  props: {
    movie: {
      type: Object,
      required: true,
    },
  },
  computed: {
    imageUrl() {
      const baseUrl = "https://image.tmdb.org/t/p/original";
      return baseUrl + this.movie.poster_path;
    },
  },
};
</script>

<style scoped></style>
