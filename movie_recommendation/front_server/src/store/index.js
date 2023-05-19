import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    movies: [],
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
  },
  actions: {
    fetchMovieDetails({ commit }, movieId) {
      axios
        .get(`${API_URL}/api/v1/movies/list/${movieId}`)
        .then((response) => {
          const movieData = response.data[0];
          commit("addMovie", movieData);
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  modules: {},
});
