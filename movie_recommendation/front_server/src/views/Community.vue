<template>
  <div class="container">

    <h1 class="header">자유 게시판</h1>
    <table>
      <thead>
        <tr>
          <th scope="col" class="col-id">#</th>
          <th scope="col" class="col-title">제목</th>
          <th scope="col" class="col-star"><i class="fas fa-star"></i></th>
          <th scope="col" class="col-author">작성자</th>

        </tr>
      </thead>

      <tbody>
        <tr class="community-item" v-for="community in communities" :key="community.id">
          <td>{{ community.id }}</td>
          <td class="col-title" @click="goDetail(community)">
            {{ community.title }}
          </td>
          <td></td>
          <td class="col-author" @click="goProfile(community)">
            {{ community.userName }}
          </td>
          <td>{{ community.time }}</td>
        </tr>
      </tbody>
    </table>
    <button class="add-button" @click="goCreate">글 작성</button>
  </div>
</template>

<style>
  .container {
    max-width: 90%;
    margin: auto;
    padding: 2rem;
  }

  .header {
    text-align: left;
    font-size: 30px;
    margin-bottom: 1.5rem;
    color: white;
    font-weight: bold;
  }

  table {
    width: 100%;
    margin-bottom: 1.5rem;
    border-collapse: collapse;
    font-size: 1.5rem;
  }

  th,
  td {
    padding: 1rem;
    border: 1px solid #dee2e6;
    text-align: left;
  }

  .col-title {
    width: 60%;
    color: white;
    text-align: left;
  }

  .col-author {
    color: white;
    margin-right: 10px;
    text-align: left;
  }

  .author {
    margin-right: 50px;
  }

  .add-button {
    display: block;
    width: 100%;
    padding: 1rem;
    font-size: 1.5rem;
    font-weight: 400;
    color: #fff;
    background-color: #007bff;
    border: 1px solid #007bff;
    text-align: center;
    white-space: nowrap;
    cursor: pointer;
  }

  .add-button:hover {
    color: #fff;
    background-color: #0069d9;
    border-color: #0062cc;
  }

  .community-item {
    border-bottom: 1px solid #dee2e6;
  }

  .id {
    text-align: left;

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
          name: "profile",
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