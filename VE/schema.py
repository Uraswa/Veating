import graphene
from accounts.graphql.query import AccountsQuery
from accounts.graphql.mutations import *


class MainQuery(AccountsQuery, graphene.ObjectType):
    pass


class Mutations(graphene.ObjectType):
    userReg = UserRegMutation.Field()
    userLogin = UserLoginMutation.Field()
    userReset = UserResetPassword.Field()
    userNewPass = NewPasswordMutation.Field()


schema = graphene.Schema(query=MainQuery, mutation=Mutations)
