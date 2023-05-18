<template>
  <div class="movie-item">
    <img :src="movie.poster" :alt="movie.title" />
    <h3>{{ movie.title }}</h3>
    <p>{{ movie.description }}</p>
    <p>아이템입니다</p>
  </div>
</template>

<script>
export default {
  name: "movieListItem",
  props: {
    movie: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped></style>
