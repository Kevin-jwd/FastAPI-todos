# FastAPI 에서는 정의된 데이터만 전송되도록 요청 바디를 검증할 수 있다. -> 데이터가 적절한지 확인, 악의적인 공격 위험을 줄여줌
# FastAPI에서 모델은 데이터가 어떻게 전달되고 처리돼야 하는지를 정의하는 구조화된 클래스
# 모델은 pydantic의 BaseModel 클래스의 하위 클래스로 생성됨.

from pydantic import BaseModel

# pydantic의 BaseModel 클래스의 하위 클래스로 정의된 PacktBook 모델
# 네 개의 필드를 가짐.
class PacktBook(BaseModel):
    id:int
    Name:str
    Publishers:str
    Isbn:str

# # 모델 중첩해서 정의 가능
# class Item(BaseModel):
#     item:str
#     status:str

# class Todo(BaseModel):
#     id:int
#     item:Item

# Todo 모델
# 두 개의 필드를 가짐
class Todo(BaseModel):
    id: int
    item: str

