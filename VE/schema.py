import graphene
from accounts.graphql.query import AccountsQuery


class MainQuery(AccountsQuery,graphene.ObjectType):
    pass


schema = graphene.Schema(query=MainQuery)