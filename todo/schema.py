import graphene
from todo_list import todoSchema


class Query(todoSchema.TodoQuery, graphene.ObjectType):
    pass


class Mutation(todoSchema.todoMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
