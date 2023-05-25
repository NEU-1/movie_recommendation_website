<template>
  <div class="search-bar">
    <input
      type="text"
      v-model="searchText"
      placeholder="검색할 영화제목을 쓰세요"
      @keyup.enter="search"
    />
    <button @click="search">검색</button>
    <div v-for="movie in movies" :key="movie.movie_id">
      <router-link :to="`/movies/${movie.movie_id}`">{{ movie.title }}</router-link>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      searchText: "",
      movies: [],
    };
  },
  methods: {
    search() {
      if (this.searchText === "") {
        alert("검색어를 입력하세요.");
      } else {
        const movieTitle = this.searchText;
        console.log("검색어:", movieTitle);
        // this.$router.push({ name: "moviedetail", params: { id: movieTitle } });
        this.$router.push({ name: "searchresults", query: { q: movieTitle } });
      }
  },
},
};
</script>
<style scoped>
.search-bar {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 100px;
  padding: 10px;
}

input {
  padding: 5px;
  margin-right: 5px;
  width: 400px;
  height: 70px;
  margin-bottom: 300px;
}

button {
  padding: 10px 10px;
  margin-bottom: 300px;
  width: 100px;
  height: 70px;
}
</style>
