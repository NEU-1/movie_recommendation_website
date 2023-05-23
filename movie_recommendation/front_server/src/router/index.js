import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "@/views/HomeView.vue";
import MovieView from "@/views/MovieView.vue";
import MovieRanking from "@/views/MovieRanking.vue";
import Community from "@/views/Community.vue";
import MovieDetail from "@/views/MovieDetail.vue";
import LoginView from "@/views/LoginView.vue";
import SignupView from "@/views/SignupView";
import CommunityFormView from "@/components/CommunityFormView.vue";
import SearchResults from "@/components/SearchResults.vue";
import ProFile from "@/views/ProFile.vue";
import NotFound404 from "@/views/NotFound404.vue";
import CommunityDetail from "@//components/CommunityDetail.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/movies/",
    name: "movieview",
    component: MovieView,
  },
  {
    path: "/ranking/",
    name: "movieranking",
    component: MovieRanking,
  },
  {
    path: "/community/",
    name: "community",
    component: Community,
  },
  {
    path: "/community/create/",
    name: "CommunityCreate",
    component: CommunityFormView,
  },
  {
    path: "/community/:community_pk/",
    name: "CommunityDetail",
    component: CommunityDetail,
  },
  {
    path: "/movies/:id/",
    name: "moviedetail",
    component: MovieDetail,
    props: true,
  },
  {
    path: "/login/",
    name: "login",
    component: LoginView,
  },
  {
    path: "/signup/",
    name: "signup",
    component: SignupView,
  },
  {
    path: "/search/",
    name: "searchresults",
    component: SearchResults,
  },
  {
    path: "/profile/:user_pk/",
    name: "ProFile",
    component: ProFile,
  },
  {
    path: "/404/",
    name: "NotFound404",
    component: NotFound404,
  },
  {
    path: "/signupgenre/",
    name: "signupgenre",
    component: SignupGenre,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
