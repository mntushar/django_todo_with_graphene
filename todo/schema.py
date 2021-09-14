import graphene
from todo_list.schema import*


class Query(TodoQuery, graphene.ObjectType):
    pass


class Mutation(Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)