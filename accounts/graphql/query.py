import graphene
from graphene_django.types import DjangoObjectType
from accounts.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ['name', 'id', 'avatar']


class AccountsQuery(graphene.ObjectType):

    test1 = graphene.String()
    users = graphene.List(UserType)

    def resolve_test1(self, info, **kwargs):
        return 'test1'

    def resolve_users(self, info, **kwargs):
        return User.objects.all()
