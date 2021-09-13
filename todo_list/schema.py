import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import*


#todo list query 
class TodoView(DjangoObjectType):
    class Meta:
        model = TodoList
        fields = '__all__'

class TodoQuery(graphene.ObjectType):
    todoList = DjangoListField(TodoView)

    def resolve_all_todo(root, info):
        return TodoList.object.get(title=2) 