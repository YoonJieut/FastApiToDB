# 스켈레톤 만들기

- APP SERVER : app router 방식
- REST API SERVER : fast api 어떻게 쓸까? (flask, express와 다르지 않음)
  - 왜 하필 이거일까?
    - Django : mvt방식이라 템플릿 찍어냄
    - flask : 마이크로, 비동기 x
  - 어떻게 돌아갈지 확인
- DB : mariaDB
  - CRUD 테스팅
  - 매개변수 까지만 만들면 된다.
- stroage
  - 스토리지 서버는 왜 필요할까?

# 관련 명령어 정리

```
python -m venv fastapitest // 생성
.\fastapitest\Scripts\activate // 입장
pip install fastapi uvicorn[standard] // fast api, uvicorn(비동기) 설치
pip install mysql-connector-python // mariadb 연결 드라이버
pip install boto3 // aws sdk for python
pip install httpx // httpx - FastAPI 의존성, http 클라이언트 라이브러리

(main.py 생성)

uvicorn main:app --reload // 애플리케이션 시작
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
uvicorn db:app --host 0.0.0.0 --port 8001 --reload
```

## py 파일 시스템 체크

- os, datetime 활용

```
import os
import re
from datetime import datetime

def nowTime():
    time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    return time

def generateYoonValues(name, index):
    for i in range(1, index):
        #현재시간
        now = nowTime()
        directory_name = f'{now}'+' '+f'{name}-{i}'

        #파일 생성
        os.makedirs(directory_name)
        directory_path = f'{directory_name}'
        # print(directory_path)
        if os.path.exists(directory_path):
            print("디렉토리가 존재합니다.")
            file_name = f'{directory_name}/{name}-{i}.txt'
            with open(file_name, 'w') as file:
                file.write('This is a sample text.')
        else:
            print("디렉토리가 존재하지 않습니다.")
            continue

```

## node.js 파일 시스템 체크
