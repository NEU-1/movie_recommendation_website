<template>
  <div class="movie-item">
    <div
      class="poster-container"
      @mouseover="showDetailsButton = true"
      @mouseleave="showDetailsButton = false"
    >
      <img :src="imageUrl" alt="Poster" class="poster-image" />
      <router-link
        v-if="showDetailsButton"
        class="details-button"
        :to="`/movies/${movie_id}`"
      >
        상세보기
      </router-link>
    </div>
    <h2 class="movie-title">{{ movie.title }}</h2>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showDetailsButton: false,
    };
  },
  methods: {},
  name: "MovieListItem",
  props: {
    movie: Object,
    movie_id: Number,
  },
  computed: {
    imageUrl() {
      const baseUrl = "https://image.tmdb.org/t/p/original";
      return baseUrl + this.movie.fields.poster_path;
    },
  },
};
</script>

<style scoped>
.movie-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
 

}

.poster-container {
  position: relative;
  text-align: center;

}

.poster-image {
  width: 360px;
  height: auto;

}

.details-button {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 10px 20px;
  font-size: 16px;
  font-weight: bold;
  color: white;
  background-color: #000;
  border: none;
  border-radius: 4px;
  opacity: 0.8;
  cursor: pointer;
}

.movie-title {
  font-weight: bold;
  color: white;
  margin-top: 10px;
}
</style>
