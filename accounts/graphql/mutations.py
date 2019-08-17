import graphene
from graphene_django.forms.mutation import DjangoModelFormMutation, DjangoFormMutation
from accounts.forms import RegisterForm, LoginForm
from .query import UserType
from accounts.models import User
from django.contrib.auth import login


class AccountsMutation:

    user = graphene.Field(UserType)
    ok = graphene.Boolean()


class UserRegMutation(AccountsMutation, DjangoModelFormMutation):

    class Meta:
        form_class = RegisterForm

    def perform_mutate(form, info):
        User.objects.create_user(
            form.cleaned_data.get('email'),
            form.cleaned_data.get('name'),
            form.cleaned_data.get('password')
        )

        return UserRegMutation(ok=True)


class UserLoginMutation(AccountsMutation, DjangoFormMutation):

    class Meta:
        form_class = LoginForm

    def perform_mutate(form, info):
        if info.context.user.is_anonymous:
            login(info.context, form.log_user)
            return UserLoginMutation(ok=True, user=form.log_user)
        return UserLoginMutation(ok=False)
