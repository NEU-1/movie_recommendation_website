<template>
  <div class="movie-detail">
    <h2><b>{{ movie.data.title }}</b></h2>
    <br/><br/>
    <div class="content">
      <div class="image-container">
        <img :src="imageUrl" alt="Poster" />
        <p>장르: {{ formattedGenres }}</p>
      </div>
      <div class="text-container">
        <p>{{ movie.data.overview }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      movie: {},
    };
  },
  async created() {
    const movie_id = this.$route.params.id;
    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/api/v1/movies/${movie_id}/`
      );
      this.movie = response.data;
    } catch (error) {
      console.error(error);
    }
  },
  computed: {
    imageUrl() {
      const baseUrl = "https://image.tmdb.org/t/p/original/";
      return baseUrl + this.movie.data.poster_path;
    },
    formattedGenres() {
      if (this.movie.data.genres && Array.isArray(this.movie.data.genres)) {
        return this.movie.data.genres.map(genre => genre.name).join(", ");
      }
      return "";
    }
  },
};
</script>

<style scoped>
  .movie-detail {
    max-width: 1400px;
    margin: 0 auto;
    padding: 20px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    font-family: Arial, sans-serif;
  }

  .movie-detail h2 {
    color: #333;
    font-size: 2.5em;
    margin-bottom: 10px;
  }

  .content {
    display: flex;
    gap: 20px;
  }

  .image-container {
    flex: 0 0 400px;
  }

  .image-container img {
    max-width: 100%;
    height: auto;
  }

  .text-container {
    flex-grow: 1;
    font-size: 20px;
  }

  .text-container p,
  .image-container p {
    color: #000; 
    line-height: 1.6;
    font-size: 1.2em;
    font-weight: bold;
    text-align: left;
  }
</style>