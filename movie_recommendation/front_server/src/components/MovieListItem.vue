<template>
  <div>
    <h2>{{ movie.title }}</h2>
    <img :src="imageUrl" alt="Poster" />
    <p>{{ movie.overview }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      movie: {}
    };
  },
  mounted() {
    // 영화 세부 내용을 조회하는 메서드를 호출합니다.
    this.fetchMovieDetails();
  },
  methods: {
    fetchMovieDetails() {
      const movieId = '영화의 ID를 입력하세요'; // 영화의 ID를 설정하세요

      axios.get(`http://127.0.0.1:8000/api/v1/movies/your-url/${movieId}`)
        .then(response => {
          const movieData = response.data[0]; // 응답이 단일 영화 객체를 포함하는 배열이라고 가정합니다.
          this.movie = {
            title: movieData.fields.title,
            description: movieData.fields.overview,
            // 표시할 다른 영화 세부 정보를 추가하세요
          };
        })
        .catch(error => {
          console.error(error);
        });
    }
  },
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
