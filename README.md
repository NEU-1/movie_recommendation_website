# MOVIE.GG

## 😎 팀원 + 업무

**FrontEnd** [김상진](<[]()>)

**Front / BackEnd** [김병민, 서지호](<[]()>)

## 🛠️ 사용한 기술 🛠

**FrontEnd** HTML / CSS / Bootstrap

**BackEnd** Python / Django

## ⚡ 구현 실패 ⚡

<br>

## 📆 프로젝트 기간

- 2023.05.18 ~ 2022.05.25
- 8 DAY

## 🎞 프로젝트 구현

### 0. 개요

- **ERD**
  ![10팀](README.assets/10팀.JPG)

- **파일트리 (개요 (일부 생략)**

```
영화 추천
├─ movie_recommendation
│  ├─ .env.local
│  ├─ back_server
│  │  ├─ accounts
│  │  │  ├─ admin.py
│  │  │  ├─ apps.py
│  │  │  ├─ migrations
│  │  │  ├─ models.py
│  │  │  ├─ serializers.py
│  │  │  ├─ tests.py
│  │  │  ├─ urls.py
│  │  │  ├─ views.py
│  │  │  ├─ __init__.py
│  │  ├─ back_server
│  │  │  ├─ asgi.py
│  │  │  ├─ settings.py
│  │  │  ├─ urls.py
│  │  │  ├─ wsgi.py
│  │  │  ├─ __init__.py
│  │  ├─ community
│  │  │  ├─ admin.py
│  │  │  ├─ apps.py
│  │  │  ├─ migrations
│  │  │  ├─ models.py
│  │  │  ├─ serializers.py
│  │  │  ├─ tests.py
│  │  │  ├─ urls.py
│  │  │  ├─ views.py
│  │  │  ├─ __init__.py
│  │  ├─ db.sqlite3
│  │  ├─ manage.py
│  │  ├─ movies
│  │  │  ├─ admin.py
│  │  │  ├─ apps.py
│  │  │  ├─ fixtures
│  │  │  │  ├─ actors.json
│  │  │  │  ├─ genre.json
│  │  │  │  └─ movies.json
│  │  │  ├─ migrations
│  │  │  ├─ models.py
│  │  │  ├─ serializers.py
│  │  │  ├─ tests.py
│  │  │  ├─ urls.py
│  │  │  ├─ views.py
│  │  │  ├─ __init__.py
│  │  └─ requirements.txt
│  ├─ front_server
│  │  ├─ babel.config.js
│  │  ├─ jsconfig.json
│  │  ├─ package-lock.json
│  │  ├─ package.json
│  │  ├─ public
│  │  │  ├─ favicon.ico
│  │  │  └─ index.html
│  │  ├─ README.md
│  │  ├─ src
│  │  │  ├─ App.vue
│  │  │  ├─ assets
│  │  │  │  ├─ 겨울왕국.png
│  │  │  │  ├─ 골드.png
│  │  │  │  ├─ 다이아.png
│  │  │  │  ├─ 동석.png
│  │  │  ├─ components
│  │  │  │  ├─ CodePen.vue
│  │  │  │  ├─ CommunityDetail.vue
│  │  │  │  ├─ CommunityFormView.vue
│  │  │  │  ├─ Footer.vue
│  │  │  │  ├─ Header.vue
│  │  │  │  ├─ LoginButton.vue
│  │  │  │  ├─ MovieList.vue
│  │  │  │  ├─ MovieListItem.vue
│  │  │  │  ├─ NavBar.vue
│  │  │  │  ├─ SearchBar.vue
│  │  │  │  └─ SearchResults.vue
│  │  │  ├─ main.js
│  │  │  ├─ router
│  │  │  │  └─ index.js
│  │  │  ├─ store
│  │  │  │  └─ index.js
│  │  │  └─ views
│  │  │     ├─ AboutView.vue
│  │  │     ├─ Community.vue
│  │  │     ├─ HomeView.vue
│  │  │     ├─ LoginView.vue
│  │  │     ├─ MovieDetail.vue
│  │  │     ├─ MovieRanking.vue
│  │  │     ├─ MovieView.vue
│  │  │     ├─ NotFound404.vue
│  │  │     ├─ ProFile.vue
│  │  │     └─ SignupView.vue
│  │  └─ vue.config.js
└─ TMDB_DATA_JSON.py
```

### 1. MOVIE

- **홈 페이지**
  ![홈](README.assets/home.JPG)

- 검색

  - 사용자가 입력한 내용에 해당되는 영화 리스트를 출력
  - 입력된 내용이 없을시 알림과 함께 이미지 출력

    <br>

- **전체 영화 페이지**
  ![전체](README.assets/all.JPG)

- 카드 디테일

  - 카드 형태로 전체 영화 목록을 제공
  - 카드 클릭시 영화 상세 페이지로 이동
  - 한 페이지에 3개씩 제공
  - Next 버튼을 눌러서 다음 목록 조회
  - 마지막 데이터에 도달시 Next 버튼 제거

    <br>

- **추천 랭킹 페이지**
  ![랭킹](README.assets/ranking.JPG)

  - 평점순위에 기반한 영화 추천
  - 제목 클릭시 영화 상세 페이지로 이동

    <br>

  ![장르](README.assets/genre.JPG)

  - 특정 장르 선택시 필터링 기능 제공

    <br>

- **영화 상세 페이지**
  ![디테일](README.assets/detail.JPG)
  - 영화의 자세한 데이터 제공
  - 예고편 재생
  - 좋아요 버튼 클릭시 프로필 창에서 확인 가능
  - 좋아하는 유저수 표시

### 2. COMMUNITY

- **게시판 페이지**
  ![커뮤](README.assets/commu.JPG)

  ![노커뮤](README.assets/nocommu.JPG) - 게시글 작성 가능 - 인증된 유저만 작성 가능 - 제목 누를시 상세 게시글 페이지로 이동 - 작성자 누를시 해당 유저의 프로필 페이지로 이동

- **게시글**
  ![게시글](README.assets/comudetail.JPG)

  - 작성자와 작성일 확인 가능
  - 상세 게시글 확인 가능
  - 수정, 삭제 가능
  - 댓글 작성 가능

### 3.

- **프로필 페이지**
  ![프로필](README.assets/profile.JPG)

  - 팔로우 버튼 클릭시 해당 유저 팔로우 가능 (본인을 팔로우시 알림창)
  - 팔로워와 팔로잉 숫자 제공
  - 좋아요 버튼을 누른 영화 개수와 해당 영화 목록 출력
  - 영화 포스터 클릭시 해당 영화의 상세 페이지로 이동

### 4.

-**로그인 페이지**
![로그인](README.assets/login.JPG)

    - 로그인 기능 제공
    - 회원가입 버튼을 눌러서 회원가입 절차 진행

## 🌄 느낀점

- 김상진
- 김병민
- 서지호

  ```
  back 과 front 간의 원할한 통신을 위해 url과 초기 erd 키들을 자세하게 설정하는게 중요하다고 느끼는 프로젝트의 연속이었다.

  처음 시작할땐 막막했지만 하다보니 어떻게든 되서 마무리 할 수 있었다.

  전체적인 복습을 통해 어느정도 배운걸 이해할수 있었고
  2학기도 실력을 많이 높일수 있으면 좋겠다.
  ```
