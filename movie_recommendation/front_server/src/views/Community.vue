<template>
  <div class="container my-5">
    <h1 class="text-center display-4 mb-5"><b>커뮤니티</b></h1>

    <div class="d-flex justify-content-end mb-4">
      <button class="btn btn-primary btn-lg" @click="goCreate">추가</button>
    </div>

    <div class="row">
      <div
        class="col-12 mb-4"
        v-for="community in communities"
        :key="community.id"
      >
        <div class="community-item">
          <div class="d-flex justify-content-center align-items-center">
            <div>
              <span class="title-label">제목: </span>
              <span class="title fw-bold" @click="goDetail(community)">
                {{ community.title }}
              </span>
            </div>
          </div>

          <div class="d-flex justify-content-between align-items-center mt-2">
            <div>
              <span class="author-label">작성자: </span>
              <span class="author text-muted" @click="goProfile(community)">
                {{ community.userName }}
              </span>
            </div>
            <div>
              <span class="views">조회수: {{ community.views }}</span>
              <span class="comments">댓글수: {{ community.comments }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.community {
  padding-bottom: 450px;
}

.community-item {
  border: 1px solid black;
  padding: 10px;
  border-radius: 5px;
}

.title-label,
.author-label {
  color: black;
}

.title,
.author {
  color: black;
  cursor: pointer;
}

.views,
.comments {
  color: black;
}
</style>

<script>
export default {
  name: "CommunityView",
  data() {
    return {
      isLogin: this.$store.getters.isLogin,
    };
  },
  computed: {
    communities() {
      return this.$store.state.communities;
    },
  },
  methods: {
    getCommunityList() {
      this.$store.dispatch("getCommunityList");
    },
    goCreate() {
      if (this.isLogin === false) {
        alert("게시글을 작성하시려면 로그인을 하세요!");
        return;
      }
      this.$router.push({ name: "CommunityCreate" });
    },
    goProfile(community) {
      this.$router.push({
        name: "MyProfile",
        params: { user_pk: community.userId },
      });
    },
    goDetail(community) {
      this.$router.push({
        name: "CommunityDetail",
        params: { community_pk: community.id },
      });
    },
  },
  created() {
    this.getCommunityList();
  },
};
</script>
