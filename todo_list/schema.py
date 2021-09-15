import graphene
from graphene_django import DjangoObjectType, DjangoListField
from django.contrib.auth.models import User
from .models import*


# declar todo model field
class TodoType(DjangoObjectType):
    class Meta:
        model = TodoList
        fields = ('id', 'title', 'date', 'text')


# todo list query
class TodoQuery(graphene.ObjectType):
    todoList = DjangoListField(TodoType)

    def resolve_todoList(root, info):
        return TodoList.objects.filter(userId=2)


# create todo
class TodoCreate(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        text = graphene.String(required=True)

    todo = graphene.Field(TodoType)

    def mutate(root, info, title, text):
        # userId = info.context.user
        user = User.objects.get(id=2)
        todo = TodoList(userId=user, title=title, text=text)
        todo.save()
        return TodoCreate(todo=todo)


# todo mutation
class Mutation(graphene.ObjectType):
    todoCreate = TodoCreate.Field()
