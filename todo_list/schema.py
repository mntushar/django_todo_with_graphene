from typing_extensions import Required
import graphene
from graphene_django import DjangoObjectType, DjangoListField
from django.contrib.auth.models import User
from .models import*


#todo model field
class TodoType(DjangoObjectType):
    class Meta:
        model = TodoList
        fields = ('id', 'title', 'date', 'text')


#user model filed
class UserType(DjangoObjectType):
    class Meta:
        model = User


#create todo
class TodoCreate(graphene.Mutation):
    class Arguments:
        title = graphene.String(Required=True)
        text = graphene.string(Required=True)

    todo = graphene.Field(TodoType)

    def mutate(root, info, title, text):
        #userId = info.context.user
        user = User.objects.get(id=2)
        todo = TodoList(userId=user, title=title, text=text)
        todo.save()
        return TodoCreate(todo=todo)


#todo list query 
class TodoQuery(graphene.ObjectType):
    todoList = DjangoListField(TodoType)

    def resolve_todoList(root, info):
        return TodoList.objects.filter(userId=2)


#todo mutation
class Mutation(graphene.ObjectType):
    createTodo = TodoCreate.Field()
         