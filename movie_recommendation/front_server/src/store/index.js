import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import router from "@/router";
import createPersistedState from "vuex-persistedstate";

const API_URL = "http://127.0.0.1:8000";

Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    movies: [],
    communities: [],
    movieDetail: null,
    token: {
      key: null,
    },
    username: null,
    profile: [],
  },
  getters: {
    getMovieById: (state) => (movieId) => {
      return state.movies.find((movie) => movie.id === movieId);
    },
    isLogin(state) {
      return state.token ? true : false;
    },
  },
  mutations: {
    addMovie(state, movie) {
      state.movies.push(movie);
    },
    GET_MOVIEDETAIL(state, movieData) {
      state.movieDetail = movieData;
    },
    GET_COMMUNITY_LIST(state, communities) {
      state.communities = communities;
    },
    SAVE_TOKEN(state, userInfo) {
      state.token = userInfo.token;
      state.username = userInfo.username;
      router.push({ name: "home" });
    },
    CLEAR_TOKEN(state) {
      state.token = null;
      state.username = null;
    },
  },
  actions: {
    getMovieDetail(context, movieId) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/${movieId}/`,
        headers: {
          Authorization: `Token ${context.state.token.key}`,
        },
      })
        .then((res) => {
          const movieData = {
            id: res.data.id,
            title: res.data.title,
          };
          context.commit("GET_MOVIEDETAIL", movieData);
          router.push("/movieDetail/");
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getCommunityList(context) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/community/create/`,
      }).then((res) => {
        context.commit("GET_COMMUNITY_LIST", res.data);
      });
    },
    signUp(context, payload) {
      let signup = false; // declare variable
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
          signup = true;
          context.commit("SAVE_TOKEN", userInfo);
        })
        .catch((err) => console.log(err.response.data));
    },
    login(context, payload) {
      let signup = false; // declare variable
      const username = payload.username;
      const password = payload.password;
      axios({
        method: "post",
        url: `${API_URL}/accounts/login/`,
        data: {
          username,
          password,
        },
      })
        .then((res) => {
          const userInfo = {
            username: payload.username,
            token: res.data.key,
          };
          signup = false;
          context.commit("SAVE_TOKEN", userInfo);
        })
        .catch((err) => console.log(err));
    },

    logout(context) {
      context.commit("CLEAR_TOKEN");
      router.push({ name: "home" }).catch((err) => {});
    },
  },
  modules: {},
});
