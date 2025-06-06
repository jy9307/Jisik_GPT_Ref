# **지식샘터 강좌 <파이썬(랭체인/스트림릿)을 활용하여 나만의 AI교사 도우미 제작, 배포하기!> 용 Repository**
     
- 본 강좌에 참여해주신 모든 선생님께 감사드립니다.     
- 최선을 다해 의미있는 강좌를 만들어보도록 하겠습니다👍👍

## 개요
     
- 본 레포지토리는 지식샘터 강좌의 참고 코드를 담고 있습니다.
- 강의를 잘 따라오셨다면 따로 다운로드 받으실 필요는 없습니다.
- 복습용, 또는 참고용으로 활용하시기 바랍니다.

## 구조
- Streamlit_practice : 본 폴더 안에는 3차시의 '스트림릿 실습'의 참고 코드가 들어있습니다.
- langchain_basic.ipynb : 본 파일은 2차시의 '랭체인 실습'의 참고 코드입니다.
- main.py : 본 파일은 4~5차시의 'AI 도우미 서비스 제작 실습'의 참고 코드입니다.


## 강의 중 필요한 코드

### 1차시

#### 터미널 공통 명령어
- 현재 디렉토리의 파일/폴더 확인하기
```bash
ls
```
     
- 다른 폴더로 이동하기
```bash
cd 폴더명
```

- 특정 폴더/파일 지우기
```bash
rm -rf 폴더/파일명
```
     
#### 가상환경 관련 명령어

- 가상 환경 생성

```bash
python -m venv env
```
       
- 가상환경 활성화(윈도우 Git Bash)       
```bash
source env/Scripts/activate
```

- 가상환경 활성화(Mac, Linux)    

```bash
source env/bin/activate
```
       
- 필요 라이브러리 설치
```bash
pip install -r requirements.txt
```
-------------
### 3차시

- 스트림릿 작동(가상환경 활성화된 상태에서)
```bash
streamlit run 파일명
```    
-------------
### 4-5차시


#### 내가 만든 서비스 서버에 업로드하기

- 현재 가상환경 세팅 저장
```bash
pip freeze > requirements.txt
```

#### Git에 내 코드 업로드하기

- 레포지토리에 깃 관련 코드 활성화
```bash
git init
```

- 내 정보 깃에 입력하기
```bash
git git config --global user.name "내이름(아무거나)"
git config --global user.email "내이메일주소@이메일.com"
```
       
- 모든 파일 깃 업로드 준비하기
```bash
git add .
```
      
- 현재 상황 온라인 저장하기(체크포인트 개념)
```bash
git commit -m "첫 커밋"
```
     
- 이 이후에 'Publish Branch'를 통해 레포지토리를 개설합니다.
       
- 만약 이후에 추가로 어떤 내용을 수정하고 다시 해당 내용을 레포지토리에 반영하고 싶을 경우 아래와 같이 순서대로 터미널에 써주세요.
```bash
git add .
git commit -m "커밋이름(자유)"
git push
```

--------------
### 6차시

- AWS EC2 인스턴스 기본 세팅

```bash
sudo apt update
```

```bash
sudo apt install python3.12-venv
```

- 내 코드 가져오기

```bash
git clone 내 레포지토리 주소
```


----------
### 자동실행세팅

```bash
sudo nano /etc/systemd/system/streamlit.service
```

- 서비스 파일 세팅
```bash
[Unit]
Description=Feedback Helper
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/폴더이름
ExecStart=/home/ubuntu/폴더이름/env/bin/streamlit run app.py --server.port=8501 --server.headless=true
Restart=always
Environment="PATH=/home/ubuntu/폴더이름/env/bin"

[Install]
WantedBy=multi-user.target
```
      
- 자동실행 세팅
```bash
sudo systemctl enable streamlit.service
sudo systemctl start streamlit.service
```