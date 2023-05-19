<template>
  <div class="home">
    <div class="poster-container">
      <img :src="randomImage" alt="" class="poster-image hoverable" />
    </div>
    <SearchBar />
  </div>
</template>

<script>
import SearchBar from "@/components/SearchBar.vue";
import img1 from "../assets/존윅.png";
import img2 from "../assets/동석.png";
import img3 from "../assets/마리오.png";
import img4 from "../assets/조커.png";

export default {
  name: "HomeView",
  components: {
    SearchBar,
  },
  data() {
    return {
      images: [img1, img2, img3, img4], // Add more image paths as needed
    };
  },
  computed: {
    randomImage() {
      const index = Math.floor(Math.random() * this.images.length);
      return this.images[index];
    },
  },
};
</script>

<style>
.poster-container {
  position: relative;
  display: inline-block;
}

.poster-image {
  width: 70%;
  height: 50%;
  transition: transform 0.3s;
}

.poster-image.hoverable:hover {
  transform: scale(1.5);
}
</style>
