from django.core.paginator import Paginator, EmptyPage
from .models import Todo
from .api import TodoSchema, APIResponseTodoListSchema, APIResponseBoolSchema, APIResponseTodoSchema
from ninja import Router


router = Router()


def translate_status(status):
    if status == "PENDING":
        return "Pending"
    if status == "IN_PROGRESS":
        return "In Progress"
    if status == "COMPLETE":
        return "Complete"


def validate(request, todo):
    errors = []
    if len(todo.title) > 255:
        errors.append("title is too long (max 255 characters)")
    if len(todo.description) > 2048:
        errors.append("title is too long (max 2048 characters)")
    return errors


@router.get("list/{status}", response=APIResponseTodoListSchema)
def todo_list(request, status: str, search: str = "", groupBy: str = "", groupByDesc: str = "", sortBy: str = "title", sortDesc: str = "false", page: int = 1, mustSort: str = "", multiSort: str = "", itemsPerPage: int = 10):
    todos = Todo.objects.filter(status=translate_status(status),)
    if search != "":
        todos = todos.filter(title__contains=search)
    if sortBy != "":
        if sortDesc:
            todos = todos.order_by("-" + sortBy)
        else:
            todos = todos.order_by(sortBy)
    paginator = Paginator(todos, itemsPerPage)
    try:
        page = paginator.page(page)
        return {"success": True, "response": {"total": todos.count(), "items": list(page.object_list)}}
    except EmptyPage:
        return {"success": True, "response": {"total": todos.count(), "items": []}}


@router.post("create", response=APIResponseTodoSchema)
def create(request, data: TodoSchema):
    if request.user.has_perm("Aid"):
        return {"success": False, "errorMessage": "You are not permitted to access this action"}
    if data.id is None:
        errors = validate(request, data)
        if len(errors) == 0:
            todo = Todo.objects.create(
                title=data.title,
                description=data.description,
                status=data.status,
                type=data.type,
            )
            return {"success": True, "response": todo}
        else:
            return {"success": False, "errorMessage": ", ".join(errors)}
    return {"success": False, "errorMessage": "cannot update todo via create"}


@router.post("update", response=APIResponseTodoSchema)
def update(request, data: TodoSchema):
    try:
        todo = Todo.objects.get(id=data.id)
        errors = validate(request, data)
        if len(errors) == 0:
            todo.title = data.title
            todo.description = data.description
            todo.status = data.status
            todo.type = data.type
            todo.save()
            return {"success": True, "response": todo}
        else:
            return {"success": False, "errorMessage": ", ".join(errors)}
    except Todo.DoesNotExist:
        return {"success": False, "errorMessage": "Todo not found"}


@router.post("delete", response=APIResponseBoolSchema)
def delete(request, data: TodoSchema):
    try:
        Todo.objects.get(id=data.id).delete()
    except Todo.DoesNotExist:
        pass
    return {"success": True, "response": True}


@router.get("{identifier}", response=APIResponseTodoSchema)
def by_id(request, identifier: int):
    try:
        todo = Todo.objects.get(id=identifier)
        return {"success": True, "response": todo}
    except Todo.DoesNotExist:
        return {"success": False, "errorMessage": "Todo not found"}
