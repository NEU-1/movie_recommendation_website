<template>
  <div>
    <h2>회원 가입</h2>
    <form @submit.prevent="submitForm">
      <label for="username">아이디</label>
      <input type="text" id="username" v-model="username" required />

      <label for="password1">비밀번호</label>
      <input type="password" id="password1" v-model="password1" required />

      <label for="password2">비밀번호 확인</label>
      <input type="password" id="password2" v-model="password2" required />

      <button type="submit">가입하기</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "SignUpView",
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    };
  },
  methods: {
    signUp() {
      const username = this.username;
      const password1 = this.password1;
      const password2 = this.password2;

      const payload = {
        username: username,
        password1: password1,
        password2: password2,
      };
      this.$store.dispatch("signUp", payload);
    },
    submitForm() {
      this.signUp();
    },
  },
};
</script>
