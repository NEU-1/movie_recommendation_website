<template>
    <div>
      <h2>{{ movie.fields.title }}</h2>
      <p>{{ movie.description }}</p>
      <button @click="toggleLike">
        좋아요 {{ isLiked ? '취소' : '누르기' }}
      </button>
      <p>11111111111</p>
  
      <h3>리뷰</h3>
      <ul>
        <li v-for="review in reviews" :key="review.id">
          {{ review.text }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        movie: {},
        isLiked: false,
        reviews: []
      };
    },
    mounted() {
      const movieId = this.$route.params.id;
  
      axios.get(`http://127.0.0.1:8000/api/v1/movies/your-url/${movieId}`)
        .then(response => {
          const movieData = response.data[0];
          this.movie = {
            title: movieData.fields.title,
            description: movieData.fields.overview,
            // 표시할 다른 영화 세부 정보를 추가하세요
          };
          console.log(response)
        })
        .catch(error => {
          console.error(error);
        });
  
      axios.get(`http://127.0.0.1:8000/api/v1/movies/${movieId}/reviews/`)
        .then(response => {
          this.reviews = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    methods: {
      toggleLike() {
        const movieId = this.$route.params.id;
  
        axios.post(`http://127.0.0.1:8000/api/v1/movies/${movieId}/postmovielike/`)
          .then(response => {
            this.isLiked = response.data.is_liked;
          })
          .catch(error => {
            console.error(error);
          });
      }
    }
  };
  </script>