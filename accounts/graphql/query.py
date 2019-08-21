import graphene
from graphene_django.types import DjangoObjectType
from accounts.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ['name', 'id', 'avatar']


class AccountsQuery(graphene.ObjectType):

    users = graphene.List(UserType,test=graphene.Boolean())
    user = graphene.Field(UserType, me=graphene.Boolean())

    def resolve_users(self, info, **kwargs):
        print(info.context.user);
        return User.objects.all()

    def resolve_user(self, info, **kwargs):
        print(info.context.user);
        is_me = kwargs.get('me')
        if is_me and info.context.user.is_authenticated:
            return info.context.user
        return None

