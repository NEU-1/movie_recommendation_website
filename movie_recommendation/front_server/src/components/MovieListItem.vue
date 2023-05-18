<template>
    <div class="movie-item">
      <img :src="movie.poster" :alt="movie.title" />
      <h3>{{ movie.title }}</h3>
      <p>{{ movie.description }}</p>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      movie: {
        type: Object,
        required: true
      }
    }
  };
  </script>
  
  <style scoped>
  .movie-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 20px;
  }
  
  .movie-item img {
    width: 200px;
    height: auto;
  }
  </style>