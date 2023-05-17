<template>
  <div id="app">
    <div class="navbar-container">
      <div class="header-container">
        <Header />
      </div>
      <NavBar />
      <LoginButton />
    </div>
    <div class="router-container">
      <router-view />
    </div>
  </div>
</template>

<script>
import NavBar from "./components/NavBar.vue";
import Header from "./components/Header.vue";
import LoginButton from "./components/LoginButton.vue";

export default {
  name: "App",
  components: {
    NavBar,
    Header,
    LoginButton,
  },
};
</script>

<style>
@import "~bootstrap/dist/css/bootstrap.css";

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  min-height: 100vh;
  background-color: rgb(83, 131, 234);
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 0;
  padding: 0;
}

.navbar-container {
  display: flex;
  justify-content: flex-end;
  padding: 10px;
  margin-bottom: 30px;
  width: 100%;
  max-width: 1500px;
  height: 70px;
}

.router-container {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 0;
}
</style>
