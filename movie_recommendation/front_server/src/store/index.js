import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import router from "@/router"; // router를 import 해야합니다. 경로는 실제 vue-router 파일 경로에 맞추어야 합니다.

const API_URL = "http://127.0.0.1:8000";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    movies: [],
    movieDetail: null, // movieDetail을 위한 상태를 추가하였습니다.
    token: {
      // 만약 token이 있다면 이런 형식으로 저장할 수 있습니다. 실제로는 로그인 절차를 통해 획득해야 합니다.
      key: "YOUR_TOKEN_HERE",
    },
  },
  getters: {
    getMovieById: (state) => (movieId) => {
      return state.movies.find((movie) => movie.id === movieId);
    },
  },
  mutations: {
    addMovie(state, movie) {
      state.movies.push(movie);
    },
    GET_MOVIEDETAIL(state, movieData) {
      // 새로운 mutation을 추가했습니다.
      state.movieDetail = movieData;
    },
  },
  actions: {
    getMovieDetail(context, movieId) {
      axios({
        method: "get",
        url: `${API_URL}/movies/${movieId}/`,
        headers: {
          Authorization: `Token ${context.state.token.key}`,
        },
      })
        .then((res) => {
          context.commit("GET_MOVIEDETAIL", res.data);
          router.push("/movieDetail/");
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },

  modules: {},
});
