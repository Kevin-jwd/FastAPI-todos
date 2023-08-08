

from fastapi import APIRouter, Path
from model import Todo, TodoItem, TodoItems

todo_router=APIRouter()             # APIRouter() 인스턴스 생성

# 내부 데이터베이스를 임시로 만들고 todos를 생성 및 추출하는 라우트 정의
todo_list=[]

@todo_router.post("/todo")     # 인스턴스에 대해 POST 요청을 처리하는 엔드포인트를 정의하는 데코레이터, 즉 '/todo'경로에 대한 POST 요청을 처리하는 함수
async def add_todo(todo:Todo) -> dict:   # 'todo'라는 딕셔너리 형식의 파라미터를 받아들여, 반환 타입으로 딕셔너리
    todo_list.append(todo)
    return{
        "message" : "Todo added successfully."
    }

@todo_router.get("/todo", response_model=TodoItems)     # 인스턴스에 대해 GET 요청을 처리하는 엔드포인트를 정의하는 데코레이터, 즉 '/todo'경로에 대한 GET 요청을 처리하는 함수
async def retrieve_todos() -> dict:    # 파라미터 없이 호출, 반환 타입으로 딕셔너리
    return{
        "todos":todo_list
    }

# 경로 매개변수 : 리소스를 식별하기 위해 API 라우팅에서 사용 -> 식별자 역할을 하며 웹 애플리케이션이 추가 처리를 할 수 있도록 연결 고리가 되기도 함.
# 앞서 할 일 (todo)를 추가하거나 모든 할 일 목록 (todo_list)를 추출하는 라우트를 만들었다.
# 아래서는 하나의 todo작업만 추출하는 새로운 라우트를 만든다.
# Path 클래스 추가 ->  FastAPI가 제공하는 클래스로, 라우트 함수에 있는 다른 인수와 경로 매개변수를 구분하는 역할을 함.
# Path 클래스는 스웨거와 ReDoc 등으로 OpenAPI 기반 문서를 자동 생성할 때 라우트 관련 정보를 함께 문서화하도록 도움.
# 첫 인수로 None 또는 ...을 받을 수 있다. 
# 첫 번째 인수가 ...이면 경로 매개변수를 반드시 지정해야 함. 또한 경로 매개변수가 숫자이면 수치 검증을 위한 인수를 지정할 수 있다.
# 예를 들어 gt(greater than), le와 같은 검증 기호를 사용할 수 있다. 이를 통해 경로 매개변수에 사용된 값이 특정 범위에 있는 숫자인지 검증이 가능.

@todo_router.get("/todo/{todo_id}")     # {todo_id} : 경로 매개변수 -> 애플리케이션이 지정한 ID와 일치하는 todo 작업을 반환할 수 있다.
async def get_single_todo(todo_id: int=Path(..., title="The ID of the todo to retrieve.")):     
    for todo in todo_list:
        if todo.id == todo_id:
            return{
                "todo" : todo
            }
    return {
        "message" : "Todo with supplied ID doesn't exist."
    }

# 쿼리 매개변수 : 선택 사항이며 보통 URL에서 ? 뒤에 나옴.
# 제공된 쿼리를 기반으로 특정한 값을 반환하거나 요청을 필터링할 때 사용된다.
# 쿼리는 라우트 처리기의 인수로 사용되지만 경로 매개변수와 다른 형태로 정의된다.
# 예를 들어 아래와 같이 FastAPI Query 클래스의 인스턴스를 만들어서 라우트 처리기의 인수로 쿼리를 정의할 수 있음.

# async query_route(query:str=Query(None)):
#   return query

# todo를 변경하기 위한 라우트 추가
@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data:TodoItem, todo_id:int=Path(..., title="The ID of the todo to be updated."))->dict:
    for todo in todo_list:
        if todo.id==todo_id:
            todo.item=todo_data.item
            return{
                "message":"Todo updated successfully."
            }
    return{
        "message":"Todo with supplied ID doesn't exist."
    }

# 삭제를 위한 DELETE 라우트 추가
@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id:int)->dict:
    for index in range(len(todo_list)):
        todo=todo_list[index]
        if todo.id==todo_id:
            todo_list.pop(index)
            return{
                "message":"Todo deleted successfully."
            }
    return{
        "message":"Todo with supplied ID doesn't exist."
    }

@todo_router.delete("/todo")
async def delete_all_todo()->dict:
    todo_list.clear()
    return{
        "message":"Todos deleted successfully."
    }

## curl 실행 시 Not found 
## APIRouter 클래스는 FastAPI 클래스와 동일한 방식으로 작동
## uvicorn은 APIRouter() 인스턴스를 사용해서 애플리케이션을 실행할 수 없다.
## APIRouter 클래스를 사용해 정의한 라우트를 FastAPI() 인스턴스에 추가해야 외부에서 접근 가능
