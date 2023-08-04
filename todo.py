

from fastapi import APIRouter

todo_router=APIRouter()             # APIRouter() 인스턴스 생성

# 내부 데이터베이스를 임시로 만들고 todos를 생성 및 추출하는 라우트 정의
todo_list=[]

@todo_router.post("/todo")     # 인스턴스에 대해 POST 요청을 처리하는 엔드포인트를 정의하는 데코레이터, 즉 '/todo'경로에 대한 POST 요청을 처리하는 함수
async def add_todo(todo:dict) -> dict:   # 'todo'라는 딕셔너리 형식의 파라미터를 받아들여, 반환 타입으로 딕셔너리
    todo_list.append(todo)
    return{
        "message" : "Todo added successfully."
    }

@todo_router.get("/todo")     # 인스턴스에 대해 GET 요청을 처리하는 엔드포인트를 정의하는 데코레이터, 즉 '/todo'경로에 대한 GET 요청을 처리하는 함수
async def retrieve_todos() -> dict:    # 파라미터 없이 호출, 반환 타입으로 딕셔너리
    return{
        "todos":todo_list
    }