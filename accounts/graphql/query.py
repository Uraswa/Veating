import graphene
from graphene_django.types import DjangoObjectType
from accounts.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ['name', 'id', 'avatar']


class AccountsQuery(graphene.ObjectType):

    users = graphene.List(UserType)
    user = graphene.Field(UserType, me=graphene.Boolean())

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_user(self, info, **kwargs):
        is_me = kwargs.get('me')
        if is_me:
            return info.context.user
