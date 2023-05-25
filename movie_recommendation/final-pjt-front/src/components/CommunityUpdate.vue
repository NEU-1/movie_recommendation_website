<template>
  <div class="container mt-5">
    <h1 class="text-center mb-4">커뮤니티 글 수정</h1>
    <div class="row justify-content-center">
      <div class="col-12 col-md-8">
        <form @submit.prevent="updateCommunity">
          <div class="mb-3">
            <input
              v-model.trim="newTitle"
              type="text"
              class="form-control"
              placeholder="제목"
            />
          </div>
          <div class="mb-3">
            <textarea
              v-model.trim="newContent"
              rows="20"
              class="form-control"
              placeholder="내용을 입력하세요."
            ></textarea>
          </div>
          <div class="d-grid gap-2">
            <button type="submit" class="btn btn-primary">수정 완료</button>
          </div>
        </form>
        <div class="d-grid gap-2 mt-3">
          <router-link
            :to="{
              name: 'CommunityDetail',
              params: { community_pk: communityId },
            }"
            class="btn btn-secondary"
            >뒤로가기</router-link
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "CommunityUpdate",
  data() {
    return {
      communityId: this.$route.params.community_pk.toString(),
      newTitle: "",
      newContent: "",
    };
  },
  methods: {
    updateCommunity() {
      axios({
        method: "put",
        url: `${API_URL}/api/v1/community/update/${this.communityId}/`,
        data: {
          id: this.communityId,
          title: this.newTitle,

          content: this.newContent,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          this.$router.push({
            name: "CommunityDetail",
            params: { community_pk: this.communityId },
          });
        })
        .catch((err) => console.log(err));
    },
  },
};
</script>

<style>
.text-center {
  color: white;
}
</style>
