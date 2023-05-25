<template>
  <div class="movie-item swiper-container">
    <div class="swiper-wrapper">
      <MovieListItem
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
        :movie_id="movie.pk"
        class="swiper-slide"
      />
    </div>

    <div class="swiper-pagination"></div>

    <div class="swiper-button-next"></div>
    <div class="swiper-button-prev"></div>
  </div>
</template>

<script>
import Swiper from "swiper";
import "swiper/swiper-bundle.css";
import MovieListItem from "@/components/MovieListItem";

export default {
  name: "MovieList",

  components: {
    MovieListItem,
  },

  props: {
    movies: {
      type: Array,
      required: true,
    },
  },

  mounted() {
    new Swiper(".swiper-container", {
      slidesPerView: 3,
      spaceBetween: 10,
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },
    });
  },
};
</script>

<style scoped>
@import "swiper/swiper-bundle.css";

.movie-item {
  width: 100%;
  height: 100%;
}

.swiper-slide {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
