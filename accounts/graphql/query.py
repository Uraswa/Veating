import graphene
from graphene_django.types import DjangoObjectType
from accounts.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ['name', 'id', 'avatar']


class AccountsQuery(graphene.ObjectType):

    logged = graphene.Field(UserType)
    users = graphene.List(UserType)

    def resolve_logged(self, info):
        return info.context.user

    def resolve_users(self, info, **kwargs):
        return User.objects.all()
