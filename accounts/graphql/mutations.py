import graphene
from graphene_django.forms.mutation import DjangoModelFormMutation, DjangoFormMutation
from accounts.forms import RegisterForm, LoginForm, ResetForm, NewPasswordForm
from .query import UserType
from accounts.models import User
from django.contrib.auth import login, logout
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.template.loader import render_to_string
from VE.settings import HOSTNAME, PROTOCOL


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


class UserResetPassword(AccountsMutation, DjangoFormMutation):

    class Meta:
        form_class = ResetForm

    def perform_mutate(form, info):
        while True:
            activation_key = get_random_string(length=60)
            try:
                if not User.objects.get(activate_key=activation_key, activated=True):
                    break
            except User.DoesNotExist:
                break

        user = form.user
        user.activate_key = activation_key
        user.save()
        msg = render_to_string('email_templates/reset_pass_email.html',
                               {'key': activation_key, 'http': PROTOCOL, 'hostname': HOSTNAME})

        send_mail(
            'Смена пароля',
            '',
            'rockavova@gmail.com',
            [form.cleaned_data['email']],
            html_message=msg
        )

        return UserResetPassword(ok=True)


class NewPasswordMutation(AccountsMutation, DjangoFormMutation):

    class Meta:
        form_class = NewPasswordForm

    def perform_mutate(form, info):
        user = form.user
        user.set_password(form.cleaned_data.get('password'))
        user.activate_key = ''
        user.save()
        login(info.context, user)
        return NewPasswordMutation(ok=True, user=user)


class UserLogoutMutation(graphene.Mutation):
    class Arguments:
        pass

    ok = graphene.Boolean()

    def mutate(self, info):
        logout(info.context)
        return UserLogoutMutation(ok=True)


