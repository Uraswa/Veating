import graphene
from graphene_django.forms.mutation import DjangoModelFormMutation, DjangoFormMutation
from accounts.forms import RegisterForm, LoginForm, ResetForm
from .query import UserType
from accounts.models import User
from django.contrib.auth import login


class AccountsErrorType(graphene.ObjectType):

    field = graphene.String()
    messages = graphene.List(graphene.String)


class AccountsMutation:

    user = graphene.Field(UserType)
    ok = graphene.Boolean()
    errors = graphene.List(AccountsErrorType)


class UserRegMutation(AccountsMutation, DjangoModelFormMutation):

    class Meta:
        form_class = RegisterForm

    def perform_mutate(form, info):
        if info.context.user.is_anonymous:
            User.objects.create_user(
                form.cleaned_data.get('email'),
                form.cleaned_data.get('name'),
                form.cleaned_data.get('password')
            )

            return UserRegMutation(ok=True)

        error = AccountsErrorType(
            field="name",
            messages=[
                "Вы должны выйти из своего акканута, прежде чем регистрировать новых пользователей"
            ]
        )
        return UserRegMutation(ok=False, errors=[error])


class UserLoginMutation(AccountsMutation, DjangoFormMutation):

    class Meta:
        form_class = LoginForm

    def perform_mutate(form, info):
        if info.context.user.is_anonymous:
            login(info.context, form.log_user)
            return UserLoginMutation(ok=True, user=form.log_user)
        error = AccountsErrorType(
            field="name",
            messages=[
                "Вы уже авторизованы на сайте"
            ]
        )
        return UserLoginMutation(ok=False, errors=[error])


class UserResetPassword(DjangoFormMutation):

    class Meta:
        form_class = ResetForm

    def perform_mutate(form, info):
        pass
