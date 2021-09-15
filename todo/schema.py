import graphene
from todo_list import schema


class Query(schema.TodoQuery, graphene.ObjectType):
    pass


class Mutation(schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
