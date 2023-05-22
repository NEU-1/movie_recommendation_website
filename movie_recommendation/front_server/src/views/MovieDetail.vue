<template>
  <div class="movie-detail" v-if="movie && movie.data">
    <h2>
      <b>{{ movie.data.fields.title }}</b>
    </h2>
    <br /><br />
    <div class="content">
      <div class="image-container">
        <img :src="imageUrl" alt="Poster" />
      </div>
      <div class="text-container">
        <p>{{ movie.data.fields.overview }}</p>
        <p>장르 : {{ getGenreName(movie.data.fields.genres) }}</p>
        <div>
          <button @click="movie_likes">좋아요</button>
          <p>좋아요 수: {{ movie.data.fields.like_movies ? movie.data.fields.like_movies.length : 0 }}</p>
        </div>
        <div class="video-container">
          <div id="player"></div>
        </div>
      </div>
    </div>
    <br />
    <br />
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      movie: {},
      player: null,
      genres: [],
    };
  },
  async created() {
    const movie_id = this.$route.params.id;
    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/api/v1/movies/${movie_id}/`
      );
      this.movie = response.data;

      const tag = document.createElement("script");
      tag.src = "https://www.youtube.com/iframe_api";
      const firstScriptTag = document.getElementsByTagName("script")[0];
      firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

      window.onYouTubeIframeAPIReady = this.onYouTubeIframeAPIReady;
    } catch (error) {
      console.error(error);
    }
    // this.getMe()
  },
  methods: {
    onYouTubeIframeAPIReady() {
      if (window.YT && window.YT.Player) {
        this.player = new window.YT.Player("player", {
          videoId: this.movie.data.fields.youtube_key,
          width: 560,
          height: 315,
          playerVars: {
            autoplay: 1,
            controls: 1,
            modestbranding: 1,
            rel: 0,
            showinfo: 0,
            fs: 1,
          },

        });
      } else {
        setTimeout(this.onYouTubeIframeAPIReady, 100);
      }
    },

    getGenreName(genreId) {
      const genreNames = this.genres
        .filter((genre) => this.movie.data.fields.genres.includes(genre.pk))
        .map((genre) => genre.fields.name);
      return genreNames.join(", ");
    },

    async movie_likes() {
      try {
        const response = await axios.post(
          `http://127.0.0.1:8000/api/v1/movies/${this.movie.data.pk}/likes/`,
          {},
          {
            headers: {
              Authorization: `Token ${this.$store.state.token}`
            }
          }
        );

        this.$set(this.movie.data.fields, 'like_movies', response.data.like_movies);
      } catch (error) {
        console.error(error);
      }
    },


  },
  async mounted() {
    try {
      const response = await axios.get(
        "http://127.0.0.1:8000/api/v1/movies/genre/",
      );
      this.genres = response.data;
      if (this.movie.data && this.movie.data.fields.youtube_key) {
        this.onYouTubeIframeAPIReady();
      }
    } catch (error) {
      console.error(error);
    }
  },
  computed: {
    imageUrl() {
      const baseUrl = "https://image.tmdb.org/t/p/original/";
      return baseUrl + this.movie.data.fields.poster_path;
    },
    formattedGenres() {
      if (
        this.movie.data.fields.genres &&
        Array.isArray(this.movie.data.fields.genres)
      ) {
        return this.movie.data.fields.genres
          .map((genre) => genre.name)
          .join(", ");
      }
      return "";
    },
  },
  beforeDestroy() {
    if (this.player) {
      this.player.destroy();
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
  color: white;
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

.video-container iframe {
  width: 100%;
  height: 315px;
}
</style>
