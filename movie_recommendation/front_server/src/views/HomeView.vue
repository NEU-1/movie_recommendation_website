<template>
  <div class="home">
    <img src="../assets/동석-removebg-preview.png" alt="" />
    <SearchBar />
  </div>
</template>

<script>
// @ is an alias to /src
import SearchBar from "@/components/SearchBar.vue";
import imgg from "../assets/동석-removebg-preview.png";

export default {
  name: "HomeView",
  components: {
    SearchBar,
    imgg,
  },
};
</script>

<style>
img {
  width: 50%;
  height: 50%;
}
</style>
