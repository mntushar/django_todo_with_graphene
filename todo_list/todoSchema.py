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

    def resolve_todoList(self, info):
        return TodoList.objects.filter(userId=2)


# create todo
class TodoCreate(graphene.Mutation):
    message = graphene.String()

    class Arguments:
        title = graphene.String(required=True)
        text = graphene.String(required=True)

    def mutate(self, info, title, text):
        # userId = info.context.user
        user = User.objects.get(id=2)
        todo = TodoList(userId=user, title=title, text=text)
        todo.save()
        return TodoCreate(message='Create Success')


# update todo item
class updateTodo(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String(required=True)
        text = graphene.String(required=True)

    todo = graphene.Field(TodoType)

    def mutate(self, info, id, title, text):
        todo = TodoList.objects.get(id=id)
        todo.title = title
        todo.text = text
        todo.save()
        return updateTodo(todo=todo)


# delete todo
class deleteTodo(graphene.Mutation):
    message = graphene.String()

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        todo = TodoList.objects.get(id=id)
        todo.delete()
        return deleteTodo(message='Delete Successful')


# todo mutation
class todoMutation(graphene.ObjectType):
    todoCreate = TodoCreate.Field()
    todoUpdate = updateTodo.Field()
    todoDelete = deleteTodo.Field()
