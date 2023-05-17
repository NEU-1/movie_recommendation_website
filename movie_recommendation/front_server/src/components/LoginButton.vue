<template>
  <div>
    <button class="login-button" @click="showLoginModal">로그인</button>
    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <span class="close" @click="closeLoginModal">&times;</span>
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
        </form>
      </div>
    </div>
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
