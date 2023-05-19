import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "@/views/HomeView.vue";
import MovieView from "@/views/MovieView.vue";
import MovieRanking from "@/views/MovieRanking.vue";
import Community from "@/views/Community.vue";
import MovieDetail from "@/views/MovieDetail.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/movies",
    name: "movieview",
    component: MovieView,
  },
  {
    path: "/ranking",
    name: "movieranking",
    component: MovieRanking,
  },
  {
    path: "/community",
    name: "community",
    component: Community,
  },
  {
    path: "/movies/:id",
    name: "moviedetail",
    component: MovieDetail,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
