<template>
  <div>
    <h1>Community 세부사항</h1>
    <div>
      <h2>{{ community.title }}</h2>
      <p>{{ community.content }}</p>
      <p>작성자: {{ community.userName }}</p>
      <p>작성일: {{ community.created_at }}</p>
      <p>수정일: {{ community.updated_at }}</p>
    </div>

    <h2>댓글</h2>
    <div v-if="comments.length === 0">
      <p>댓글이 없습니다.</p>
    </div>
    <div v-else>
      <ul>
        <li v-for="comment in comments" :key="comment.id">
          <p>{{ comment.content }}</p>
          <p>작성자: {{ comment.userName }}</p>
          <p>작성일: {{ comment.created_at }}</p>
        </li>
      </ul>
    </div>
    <div>
      <h2>댓글 작성</h2>
      <form @submit.prevent="createComment">
        <textarea v-model.trim="commentContent" rows="4" cols="50"></textarea>
        <button type="submit">댓글 작성</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "CommunityDetail",
  data() {
    return {
      community: {},
      commentContent: null,
      communityId: this.$route.params.community_pk.toString(),
      comments: [],
    };
  },
  methods: {
    getCommunityDetail() {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/community/detail/${this.communityId}`,
      })
        .then((res) => {
          console.log(res.data);
          this.community = res.data;
        })
        .catch((err) => console.log(err));
    },
    getCommunityComment() {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/community/comments/${this.communityId}`,
      })
        .then((res) => {
          this.comments = res.data;
        })
        .catch((err) => console.log(err));
    },
    createComment() {
      console.log(this.$store.state.token);
      console.log(1111111);

      const content = this.commentContent;
      if (!content) {
        alert("내용을 입력해주세요!");
        return;
      }
      axios({
        method: "post",
        url: `${API_URL}/api/v1/community/${this.communityId}/comment_create/`,
        data: {
          content,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          this.$emit("comment_add");
          this.commentContent = "";
          this.getCommunityComment();
        })
        .catch((err) => console.log(err));
    },
  },
  created() {
    this.getCommunityDetail();
    this.getCommunityComment();
  },
};
</script>

<style></style>
