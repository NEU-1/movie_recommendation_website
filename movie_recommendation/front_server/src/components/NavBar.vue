<template>
  <nav
    class="navbar navbar-expand-lg navbar-dark"
    style="background-color: rgb(83, 131, 234)"
  >
    <ul class="navbar-nav">
      <li class="nav-item" :class="{ active: $route.path === '/' }">
        <router-link class="nav-link" to="/">홈</router-link>
      </li>
      <li class="nav-item" :class="{ active: $route.path === '/movies' }">
        <router-link class="nav-link" to="/movies">전체영화목록</router-link>
      </li>
      <li class="nav-item" :class="{ active: $route.path === '/ranking' }">
        <router-link class="nav-link" to="/ranking">랭킹</router-link>
      </li>
      <li class="nav-item" :class="{ active: $route.path === '/community' }">
        <router-link class="nav-link" to="/community">커뮤니티</router-link>
      </li>
      <li
        class="nav-item"
        :class="{ active: $route.path === '/recommendation' }"
      >
        <router-link class="nav-link" to="/recommendation">추천</router-link>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: "NavBar",
};
</script>

<style scoped>
.navbar {
  padding: 10px;
}

.navbar-nav {
  display: flex;
  align-items: center;
}

.nav-item {
  margin-right: 20px;
}

.nav-link {
  color: rgb(80, 76, 76);
  font-size: 25px;
  text-decoration: none;
}

.nav-link:hover {
  text-decoration: underline;
}

li.active {
  font-weight: bold;
  color: #fff;
}
</style>
