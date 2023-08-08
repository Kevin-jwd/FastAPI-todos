# FastAPI 에서는 정의된 데이터만 전송되도록 요청 바디를 검증할 수 있다. -> 데이터가 적절한지 확인, 악의적인 공격 위험을 줄여줌
# FastAPI에서 모델은 데이터가 어떻게 전달되고 처리돼야 하는지를 정의하는 구조화된 클래스
# 모델은 pydantic의 BaseModel 클래스의 하위 클래스로 생성됨.

from pydantic import BaseModel
from typing import List, Optional
from fastapi import Form

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
    id: Optional[int]
    item: str

    @classmethod
    def as_form(
        cls,
        item:str=Form(...)
    ):
        return cls(item=item)
    # redoc json 스키마를 올바르게 생성하기 위해 사용자가 입력해야 할 데이터의 샘플을 설정 가능
    # 샘플 데이터는 모델 클래스 안에 Config 클래스로 정의

    # 책은 03.22.23 에 출판했는데 pydantic V2가 6월 중에 출시되면서 schema_extra와 json_schema_extra를 구분하던 것이 후자로 통일되었다.
    # 책에서는 schema_extra를 사용하지만 이제는 json_schema_extra를 사용한다.
    # 출처 : https://docs.pydantic.dev/dev-v2/migration/
    class Config:
        json_schema_extra={
            "example":{
                "id":1,
                "item":"Example Schema!"
            }
        }

# UPDATE 라우트의 요청 바디용 모델 추가
class TodoItem(BaseModel):
    item:str

    class Config:
        json_schema_extra={
            "example":{
                "item":"Read the next chapter of the book."
            }
        }

class TodoItems(BaseModel):
    todos:List[TodoItem]

    class Config:
        schema_extra={
            "example":{
                "todos":[
                    {
                        "item":"Example schema 1!"
                    },
                    {
                        "item":"Example schema 2!"
                    }
                ]
            }
        }

