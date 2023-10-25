from ninja import Schema
from ninja.orm import create_schema
from typing import List
from .models import APIResponse


class TodoSchema(Schema):
    id: int = None
    title: str = None
    description: str = None
    status: str = None
    type: str = None
    created_by: str = None
    updated_by: str = None


class TodoListSchema(Schema):
    total: int = None
    items: List[TodoSchema] = None


APIResponseTodoListSchema = create_schema(APIResponse, name="APIResponseRegisterSchema", exclude=["id"], custom_fields=[("response", TodoListSchema, None)])
APIResponseTodoSchema = create_schema(APIResponse, name="APIResponseRegisterSchema", exclude=["id"], custom_fields=[("response", TodoSchema, None)])
APIResponseBoolSchema = create_schema(APIResponse, name="APIResponseRegisterSchema", exclude=["id"], custom_fields=[("response", bool, None)])
