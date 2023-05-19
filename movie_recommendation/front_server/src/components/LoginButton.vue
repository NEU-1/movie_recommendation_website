<template>
  <div>
    <router-link to="/login" class="login-button">로그인</router-link>
    <router-link to="/signup" class="signup-button">회원가입</router-link>
  </div>
</template>

<script>
export default {
  name: "LoginButton",
  data() {
    return {
      showModal: false,
      username: "",
      password: "",
    };
  },
  methods: {
    showLoginModal() {
      this.showModal = true;
    },
    closeLoginModal() {
      this.showModal = false;
    },
    login() {
      console.log("아이디:", this.username);
      console.log("비밀번호:", this.password);
      // 로그인 로직을 수행합니다.
      // ...
      this.closeLoginModal();
    },
  },
};
</script>

<!-- ...your styles... -->
<style scoped>
.login-button {
  padding: 10px 20px;
  background-color: black;
  color: #fff;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
}

.modal {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
}

.modal-content {
  background-color: #fff;
  padding: 20px;
  width: 300px;
}

.close {
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 18px;
  font-weight: bold;
  cursor: pointer;
}

.form-group {
  margin-bottom: 10px;
}

label {
  display: block;
  font-weight: bold;
}

input {
  width: 100%;
  padding: 5px;
  font-size: 14px;
}

button[type="submit"] {
  padding: 10px 20px;
  background-color: black;
  color: #fff;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
}
</style>
