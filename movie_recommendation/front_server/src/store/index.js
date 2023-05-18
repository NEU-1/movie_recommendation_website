import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  getters: {},
  mutations: {},
  actions: {
    getMovies(context) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/`,
      })
        .then((res) => console.log(res, context))
        .catch((err) => console.log(err));
    },
  },
  modules: {},
});
