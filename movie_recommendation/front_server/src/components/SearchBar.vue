<template>
  <div class="search-bar">
    <input
      type="text"
      v-model="searchText"
      placeholder="검색할 영화제목을 쓰세요"
    />
    <button @click="search">검색</button>
  </div>
</template>

<script>
export default {
  name: "SearchBar",
  data() {
    return {
      searchText: "",
    };
  },
  methods: {
    search() {
      console.log("검색어:", this.searchText);
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
