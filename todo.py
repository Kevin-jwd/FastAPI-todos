

from fastapi import APIRouter
from model import Todo

todo_router=APIRouter()             # APIRouter() 인스턴스 생성

# 내부 데이터베이스를 임시로 만들고 todos를 생성 및 추출하는 라우트 정의
todo_list=[]

@todo_router.post("/todo")     # 인스턴스에 대해 POST 요청을 처리하는 엔드포인트를 정의하는 데코레이터, 즉 '/todo'경로에 대한 POST 요청을 처리하는 함수
async def add_todo(todo:Todo) -> dict:   # 'todo'라는 딕셔너리 형식의 파라미터를 받아들여, 반환 타입으로 딕셔너리
    todo_list.append(todo)
    return{
        "message" : "Todo added successfully."
    }

@todo_router.get("/todo")     # 인스턴스에 대해 GET 요청을 처리하는 엔드포인트를 정의하는 데코레이터, 즉 '/todo'경로에 대한 GET 요청을 처리하는 함수
async def retrieve_todos() -> dict:    # 파라미터 없이 호출, 반환 타입으로 딕셔너리
    return{
        "todos":todo_list
    }

# 경로 매개변수 : 리소스를 식별하기 위해 API 라우팅에서 사용 -> 식별자 역할을 하며 웹 애플리케이션이 추가 처리를 할 수 있도록 연결 고리가 되기도 함.
# 앞서 할 일 (todo)를 추가하거나 모든 할 일 목록 (todo_list)를 추출하는 라우트를 만들었다.
# 아래서는 하나의 todo작업만 추출하는 새로운 라우트를 만든다.

@todo_router.get("/todo/{todo_id}")     # {todo_id} : 경로 매개변수 -> 애플리케이션이 지정한 ID와 일치하는 todo 작업을 반환할 수 있다.
async def get_single_todo(todo_id: int) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return{
                "todo" : todo
            }
    return {
        "message" : "Todo with supplied ID doesn't exist."
    }

## curl 실행 시 Not found 
## APIRouter 클래스는 FastAPI 클래스와 동일한 방식으로 작동
## uvicorn은 APIRouter() 인스턴스를 사용해서 애플리케이션을 실행할 수 없다.
## APIRouter 클래스를 사용해 정의한 라우트를 FastAPI() 인스턴스에 추가해야 외부에서 접근 가능
