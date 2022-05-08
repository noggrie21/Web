# 막힌 곳

### 1. Model

- `comment/models.py`에서 `movies/models.py`에 있는 Movie import 해오기
  - `from ..movies.models import Movie`하면 되는 줄 알았는데 이렇게 하면 자꾸 최상위 폴더를 너머섰다고 나와서 찾아봣더니
  - 이미 각 `app`들은 `__init__.py`파일이 있어서 그냥 `from movies.models import Movie`로 해도 되는 것이었다.

### 2. login

- `loginform`유효성 검사를 마친 후 `auth_login`으로 인증 절차

  - 인자로 `request`, `User`인스턴스를 받는데서 `auth_login(request, request.user)라고 했다가 annoymoususer어쩌고저쩌고 에러 발생
  - 생각해보면 현재 request유저는 익명유저.....그럼 도대체 어떻게 넘겨야하나 유저 정보는 loginform에 있는데 loginform을 넣는 건 아니고......
  - 결국 생각이 안나서 스켈레톤 코드를 봤는데 AuthenticationForm클래스에 정의된 `get_user()`메소드를 사용하면 되는 것이었다.....
  - 저번에도 여기서 막혔었ㄴㄴ데...또......

  

### 3. git branch 명령어

```bash
# (로그인) 브랜치 생성 및 이동
git branch -c login

# 브랜치 병합
1. 가장 먼저 master로 이동!
git switch master

2. 병합!
git merge login

3. 삭제! # 잘 삭제되었는 지 git switch login 쳤더니 전에 존재했던 거라고 다시 살려서 이동시키더라....ㅋㅋㅋㅋㅋㅋ당황잼
git branch login


# 브랜치 목록 살펴보기
git log --branches --graph --oneline
```

