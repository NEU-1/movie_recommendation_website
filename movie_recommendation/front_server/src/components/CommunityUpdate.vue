<template>
    <div>
      <h1>커뮤니티 글 수정</h1>
      <form @submit.prevent="updateCommunity">
        <input v-model.trim="newTitle" type="text" placeholder="제목" />
        <textarea v-model.trim="newContent" rows="4" cols="50"></textarea>
        <button type="submit">수정 완료</button>
      </form>
      <router-link :to="{ name: 'CommunityDetail', params: { community_pk: communityId }}" class="back-button">뒤로가기</router-link>
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
            title: this.newTitle, // 수정: 입력한 제목 필드

        content: this.newContent,  // 수정할 필드: 커뮤니티의 내용
    },
          headers: {
            Authorization: `Token ${this.$store.state.token}`,
          },
        })
          .then((res) => {
            // 수정 완료 후 커뮤니티 상세 페이지로 이동합니다.
            this.$router.push({ name: "CommunityDetail", params: { community_pk: this.communityId } });
          })
          .catch((err) => console.log(err));
      },
    },
  };
  </script>
  
  <style>
  /* 스타일 설정 */
  </style>