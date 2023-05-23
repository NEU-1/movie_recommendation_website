<template>
  <div class="container">
    <div class="row"></div>

    <div class="title1">
      <h2>게시글 작성</h2>
    </div>
    <br />
    <form @submit.prevent="createCommunity">
      <div>
        <input
          type="text"
          class="form-control"
          id="title"
          aria-describedby="titleHelp"
          v-model.trim="title"
          placeholder="제목"
        />
      </div>
      <div class="mb-3 py-3">
        <textarea
          type="text"
          class="form-control"
          id="content"
          v-model.trim="content"
          placeholder="내용"
          style="height: 500px"
        ></textarea>
      </div>
      <div class="button-group">
        <router-link :to="{ name: 'community' }">
          <button class="btn btn-primary">뒤로가기</button>
        </router-link>
        <button type="submit" class="btn btn-primary">등록</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "CommunityForm",
  data() {
    return {
      title: null,
      content: null,
    };
  },
  methods: {
    createCommunity() {
      const title = this.title;
      const content = this.content;
      if (!title) {
        alert("제목을 입력해주세요!");
        return;
      } else if (!content) {
        alert("내용을 입력해주세요!");
        return;
      }
      axios({
        method: "post",
        url: `${API_URL}/api/v1/community/create/`,
        data: {
          title,
          content,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          // console.log(res.data)
          this.$router.push({
            name: "CommunityDetail",
            params: { community_pk: res.data.id },
          });
        })
        .catch((err) => console.log(err));
    },
  },
};
</script>

<style scoped>
.container {
  max-width: 740px;
  margin: 0 auto;
}
.form-control {
  width: 700px;
}
.title1 {
  text-align: left;
  font-size: 30px;
  font-weight: bold;
  color: white;
}
.button-group {
  text-align: right;
  margin-right: 10px;
}
.button-group button {
  margin-left: 10px; /* 버튼 사이의 간격을 조정할 수 있습니다 */
}
</style>
