import graphene
from graphene_django.forms.mutation import DjangoModelFormMutation
from accounts.forms import RegisterForm
from .query import UserType
from accounts.models import User


class UserRegMutation(DjangoModelFormMutation):
    class Meta:
        form_class = RegisterForm

    user = graphene.Field(UserType)
    ok = graphene.Boolean()

    def perform_mutate(form, info):
        User.objects.create_user(
            form.cleaned_data.get('email'),
            form.cleaned_data.get('name'),
            form.cleaned_data.get('password')
        )

        return UserRegMutation(ok=True)
