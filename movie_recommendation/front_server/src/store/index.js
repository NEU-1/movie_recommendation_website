import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import router from "@/router"; // router를 import 해야합니다. 경로는 실제 vue-router 파일 경로에 맞추어야 합니다.

const API_URL = "http://127.0.0.1:8000";
const API_KEY = "a37782b08f823354bf51e4e5f7c07775";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    movies: [],
    movieDetail: null, // movieDetail을 위한 상태를 추가하였습니다.
    token: {
      key: "YOUR_TOKEN_HERE",
    },
    username: null,
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
      state.movieDetail = movieData;
    },
    SAVE_TOKEN(state, userInfo) {
      state.token = userInfo.token;
      state.username = userInfo.username;
      router.push({ name: "Home" });
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
    signUp(context, payload) {
      axios({
        method: "post",
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        },
      })
        .then((res) => {
          const userInfo = {
            username: payload.username,
            token: res.data.key,
          };
          context.commit("SAVE_TOKEN", userInfo);
        })
        .catch((err) => console.log(err));
    },
  },

  modules: {},
});
