## Todo-list
todolist 개발


## 환경 구성
# [window 환경]

# <기본 설치>
1. pychan(3.9 이상 설치)
2. ananconda 설치

# <Django 설치>
1. cmd 열기
2. 가상환경 셋팅 할 폴더로 이동
3. 가상환경 확인 명령어 
    : conda env list
4. 가상환경 생성 
    : conda create --name todolist_env python=[본인 python 버전]
    (python 버전 확인) python --version
5.  가상환경 활성화
    : activate todolist_env
    (비 활성화) deactivate
6. Django 설치
    : python -m pip install Django
7. Django 설치 확인
    : python -m django --verion
    
# <git 프로젝트 구성>
1. github에서 레포지토리 생성하기
2. 생성된 레포지토리 링크 복사
3. 위에서 설치 한 가상환경에서 git clone 만들기
    : git clone <2번에서 복사한 레포지토리 링크 입력>
    -> 여기서 git@github.com: Permission denied (publickey).
              fatal: Could not read from remote repository. 에러 발생하면 아래 git ssh 설정 수행
4.  생성 된 레포지토리 안으로 이동하여 아래 명령어 실행
     : django-admin startproject <프로젝트 명> 
5.  .gitignore 파일 생성(깃 허브에 파일 업로드 시 올리지 않을 파일을 .gitignore파일 안에 작성하면 됨)

# <git ssh 설정>
1.  git bash열기
2.  ssh-keygen -t rsa -C "github 아이디" 입력
3.  2번 입력 시 key 파일이 저장한 위치가 출력 됨
4.  비밀번호를 입력하고 싶으면 입력하고, 아니면 enter를 누름
5.  github 페이지에서 setting로 이동
6.  왼쪽 메뉴에서 ssh and GPG keys 클릭
7.  new SSH key 선택
8.  3번에서 출력됐던 저장된 위치로 이동하여 id_rsa.pub파일을 메모장으로 열어 복사
9.  복사한 것을 7번을 실행했을 때 뜬 팝업창에 입력 후 저장
10.  git bash에서 ssh -T git@github.com 입력
11.  successfully authenticated 가 뜨면 성공
