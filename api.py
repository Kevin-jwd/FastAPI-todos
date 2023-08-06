# 이 방식은 라우팅 중에 단일 경로만 고려하는 애플리케이션에서 사용
# 고유한 함수를 처리하는 각각의 라우트가 FastAPI() 인스턴스를 사용하는 경우 애플리케이션은 한 번에 여러 라우트를 처리하지 못함.
# uvicorn이 하나의 엔트리 포인트만 실행가능하기 때문

from fastapi import FastAPI
from todo import todo_router

app=FastAPI()            # app변수에 FastAPI를 초기화해서 라우트 생성

# 데코레이터를 사용해 처리 유형을 정의하고
# 라우트가 호출됐을 떄 실행할 처리를 함수로 작성
# 아래 코드는 GET 유형의 요청을 받아 환영 메시지를 반환하는 "/" 라우트를 만듦
@app.get("/")                         # 데코레이터 적용
async def welcome() -> dict:          # async : 비동기 함수, -> dict : 함수의 반환 타입
    return {
        "message" : "Hello World"
    }

app.include_router(todo_router)       # FastAPI() 인스턴스의 include_router() 메서드 사용

## 서버 실행 
## 터미널 : uvicorn api:app --port 8000 --reload
## file:instance : FastAPI 인스턴스가 존재하는 파이썬 파일과 FastAPI 인스턴스를 가지고 있는 변수를 지정
## --port PORT : 애플리케이션에 접속할 수 있는 포트 번호 지정
## --reload : 선택적 인수, 파일이 변경될 때마다 애플리케이션 재시작
## cmd : curl (Client for URLs) http://localhost:8000/