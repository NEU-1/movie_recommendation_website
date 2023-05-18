import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "@/views/HomeView.vue";
import MovieView from "@/views/MovieView.vue";
import MovieRanking from "@/views/MovieRanking.vue";
import Community from "@/views/Community.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/movies",
    name: "MovieView",
    component: MovieView,
  },
  {
    path: "/ranking",
    name: "movieRanking",
    component: MovieRanking,
  },
  {
    path: "/community",
    name: "community",
    component: Community,
  },

  // {
  //   path: '/about',
  //   name: 'about',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  // }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
