<template>
  <div id="header">
    <router-link class="home-link" to="/">MV.GG</router-link>
  </div>
</template>

<script>
export default {};
</script>

<style>
#header {
  position: fixed;
  top: 0;
  left: 0;
  padding: 10px;
}

.home-link {
  font-size: 30px;
  font-weight: bold;
  color: #fff;
  margin: 0;
  text-decoration: none;
}

.home-link:hover {
  text-decoration: underline;
  cursor: pointer;
}
</style>
