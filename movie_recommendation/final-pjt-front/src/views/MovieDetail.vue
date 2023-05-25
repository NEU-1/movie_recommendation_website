<template>
  <div class="movie-detail" v-if="movie">
    <link
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css"
      rel="stylesheet"
    />
    <h2>
      <b>{{ movie.title }}</b>
    </h2>
    <br /><br />
    <div class="content">
      <div class="close-button-container">
        <button @click="goBack">닫기</button>
      </div>
      <div class="image-container">
        <img :src="imageUrl" alt="Poster" />

        <div class="like-section">
          <div class="container3">
            <button class="btn btn-primary" @click="movie_likes">
              좋아요:
              {{ movie.like_users ? movie.like_users.length : 0 }}
            </button>
          </div>
        </div>
      </div>
      <div class="video-container">
        <div id="player"></div>
        <br />
        <div class="container2">
          <div class="text-container">
            {{ movie.overview }}
          </div>
        </div>
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
      player: null,
      genres: [],
      like_count: null,
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
  },
  methods: {
    goBack() {
      this.$router.go(-1);
    },

    onYouTubeIframeAPIReady() {
      if (window.YT && window.YT.Player && this.movie) {
        this.player = new window.YT.Player("player", {
          videoId: this.movie.youtube_key || "",
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
    async movie_likes() {
      try {
        const movieId = this.movie.id;
        const url = `http://127.0.0.1:8000/api/v1/movies/${movieId}/likes/`;
        const headers = {
          headers: {
            Authorization: `Token ${this.$store.state.token}`,
          },
        };

        const response = await axios.post(url, null, headers);
        this.$set(this.movie, "like_users", response.data.like_users);
      } catch (error) {
        console.error(error);
      }
    },
  },
  async mounted() {
    try {
      const response = await axios.get(
        "http://127.0.0.1:8000/api/v1/movies/genre/"
      );
      this.genres = response.data;
      if (this.movie && this.movie.youtube_key) {
        this.onYouTubeIframeAPIReady();
      }
    } catch (error) {
      console.error(error);
    }
  },
  computed: {
    imageUrl() {
      const baseUrl = "https://image.tmdb.org/t/p/original/";
      return baseUrl + this.movie.poster_path;
    },
    formattedGenres() {
      if (this.movie.genres && Array.isArray(this.movie.genres)) {
        return this.movie.genres.map((genre) => genre.name).join(", ");
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
  position: relative;
  max-width: 1100px;
  width: 1100px;
  height: 900px;
  margin: 0 auto;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
  font-family: Arial, sans-serif;
}
.container2 {
  margin: 10px !important;
  padding: 10px;
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
.close-button-container {
  position: absolute;
  top: 20px;
  right: 20px;
}
.close-button-container button {
  background-color: black;
  color: white;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
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
  font-weight: bold;
  color: white;
}
.container3 {
  padding: 20px;
  font-weight: bold;
  text-align: center;
  font-size: 20px;
}
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
  margin-bottom: 10px !important;
}
</style>
