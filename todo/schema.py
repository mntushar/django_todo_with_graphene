import graphene
from todo_list.schema import*


class Query(TodoQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)