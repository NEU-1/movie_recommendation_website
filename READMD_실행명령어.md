## 가상환경 구동, 실행

python -m venv myvenv
source myvenv/Scripts/activate
pip install -r requirements.txt
pip install djangorestframework-jwt


## 파일 디렉토리 이동

### BACK

cd movie_recommendation
cd back_server

### 프론트도 동일하게

cd movie_recommendation
cd front_server


## 사전 입력

### BACK

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata actors.json
python manage.py loaddata genre.json
python manage.py loaddata movies.json

### FRONT

npm i
npm install bootstrap
npm install bootstrap-vue bootstrap


## 실행

### BACK

python manage.py runserver

### FRONT

npm run serve


## 서버 종료

deactivate

