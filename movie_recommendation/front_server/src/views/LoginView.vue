<template>
  <div class="login-view">
    <h2>로그인</h2>
    <form @submit.prevent="login">
      <div class="form-group">
        <label for="username">아이디</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div class="form-group">
        <label for="password">비밀번호</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit">로그인</button>
      <button type="button" @click="goToSignup">회원가입</button>
      <!-- 수정된 부분 -->
    </form>
  </div>
</template>

<script>
export default {
  name: "LoginView",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password
      const payload = {
        username, password
      }
      this.$store.dispatch('login', payload)
    },
    goToSignup() {
      this.$router.push("/signup");
    },
  },
};
</script>
