import graphene


class AccountsQuery(graphene.ObjectType):

    test1 = graphene.String()

    def resolve_test1(self,info,**kwargs):
        return 'test1'