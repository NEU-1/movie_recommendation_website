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

### 1. 메인 페이지

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
  - 한 페이지에 3개씩 제공
  - Next 버튼을 눌러서 다음 목록 조회
  - 마지막 데이터에 도달시 Next 버튼 제거

    <br>

- **추천 랭킹 페이지**

### 3.

### 4.

### 5.

### 6.

## 🌄 느낀점
