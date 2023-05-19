<template>
  <div>
    <h2>회원 가입</h2>
    <form @submit.prevent="submitForm">
      <label for="username">아이디</label>
      <input type="text" id="username" v-model="username" required />

      <label for="password">비밀번호</label>
      <input type="password" id="password" v-model="password" required />

      <label for="passwordConfirm">비밀번호 확인</label>
      <input
        type="password"
        id="passwordConfirm"
        v-model="passwordConfirm"
        required
      />

      <button type="submit">가입하기</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      username: "",
      password: "",
      passwordConfirm: "",
    };
  },
  methods: {
    async submitForm() {
      if (this.password !== this.passwordConfirm) {
        alert("비밀번호가 일치하지 않습니다.");
        return;
      }

      try {
        const response = await axios.post(
          "http://localhost:8000/accounts/signup/",
          {
            username: this.username,
            password: this.password,
            passwordConfirmation: this.passwordConfirm,
          }
        );

        console.log(response.data);
      } catch (error) {
        console.error(error);
        alert("회원 가입에 실패했습니다.");
      }
    },
  },
};
</script>
