<template>
  <div class="community-detail">
    <header>
      <!-- 커뮤니티 제목 -->
      {{ community.title }}
    </header>

    <div class="community-info">
      <div class="author-info">
        <!-- 작성자 정보 -->
        <p class="author">작성자:{{ community.userName }}</p>
        <p class="created-at">작성일:{{ community.created_at }}</p>
        <!-- <p>수정일: {{ community.updated_at }}</p> -->
      </div>
      <hr />

      <!-- 커뮤니티 내용 -->
      <div class="content">
        {{ community.content }}
      </div>
      <div v-if="isAuthor(community.userName)">
        <router-link :to="{ name: 'CommunityUpdate', params: { community_pk: communityId }}" class="edit-button">수정</router-link>
        <button @click="deleteCommunity">삭제</button>
      </div>
    </div>
    <router-link to="/community/" class="back-button">뒤로가기</router-link>

    <div class="asdf">댓글</div>

    <hr />

    <div v-if="comments.length === 0">
      <p>댓글이 없습니다.</p>
    </div>
    <div v-else>
      <ul class="comment-list">
        <li v-for="comment in comments" :key="comment.id">
          <p class="comment-author">{{ comment.userName }}</p>
          <p>{{ comment.content }}</p>
        </li>
      </ul>
    </div>
    <div class="comment-form" style="text-align: right">
      <form @submit.prevent="createComment">
        <textarea v-model.trim="commentContent" rows="4" cols="50"></textarea>
        <button type="submit">댓글 작성</button>
      </form>
    </div>
  </div>
</template>

<style>
.community-detail {
  padding: 20px;
  width: 1000px;
  min-height: 1000px;
  border: 2px solid #000;
  background-color: white;
}

header {
  text-align: left;
  font-weight: bold;

  font-size: 50px;
}

.author-info {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 10px;
  color: rgb(80, 76, 76);
  text-align: right;
}

.author-info p {
  margin-left: 5px;
}

.content {
  width: 900px;
  height: 500px;
  margin: 0;
  text-align: left;

  margin-bottom: 20px;
}

.comment-list {
  list-style: none;
  padding: 0;
  margin-bottom: 20px;
}

.comment-list li {
  margin-bottom: 10px;
  text-align: left;
}

.comment-form textarea {
  width: 100%;
  resize: vertical;
  margin-bottom: 10px;
}

.comment-form button {
  padding: 5px 10px;
}
.asdf {
  text-align: left;
}
</style>

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
    isAuthor(userName) {
      // console.log(this.community.userName)
      // console.log(this.$store.state.username)
    return userName === this.$store.state.username;
  },

deleteCommunity() {
  const confirmDelete = confirm("정말로 삭제하시겠습니까?");
  if (confirmDelete) {
    axios({
      method: "delete",
      url: `${API_URL}/api/v1/community/update/${this.communityId}/`,
      headers: {
        Authorization: `Token ${this.$store.state.token}`,
      },
    })
      .then(() => {
        this.$router.push("/community/");
      })
      .catch((err) => console.log(err));
  }
},

  },
  created() {
    this.getCommunityDetail();
    this.getCommunityComment();
  },
  mounted(){
    this.getCommunityComment();
  }
};
</script>
