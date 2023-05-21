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
import img5 from "../assets/스즈메.png";
import img6 from "../assets/스파이더맨.png";
import img7 from "../assets/쥬라기월드.png";
import img8 from "../assets/토토로.png";
import img9 from "../assets/트랜스포머.png";
import img10 from "../assets/해리포터.png";
import img11 from "../assets/터미네이터.png";
export default {
  name: "HomeView",
  components: {
    SearchBar,
  },
  data() {
    return {
      images: [img1, img2, img3, img4, img5, img6, img7, img8, img9,img10,img11], // Add more image paths as needed
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
  margin-right: 50px;
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
