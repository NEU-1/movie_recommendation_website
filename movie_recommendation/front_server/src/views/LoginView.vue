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
      console.log("아이디:", this.username);
      console.log("비밀번호:", this.password);

      // 이곳에 백엔드 서버와의 통신 코드를 추가해야 합니다.
      // 로그인 성공 후에는 사용자를 알맞은 페이지로 리다이렉트하거나,
      // 로그인 상태를 전역 상태로 관리하는 등의 추가 작업이 필요합니다.
    },
    goToSignup() {
      // 추가된 메소드
      this.$router.push("/signup");
    },
  },
};
</script>
