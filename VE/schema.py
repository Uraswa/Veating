import graphene
from accounts.graphql.query import AccountsQuery
from accounts.graphql.mutations import UserRegMutation


class MainQuery(AccountsQuery,graphene.ObjectType):
    pass


class Mutations(graphene.ObjectType):
    userReg = UserRegMutation.Field()


schema = graphene.Schema(query=MainQuery, mutation=Mutations)
