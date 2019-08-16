import os
import django



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "VE.settings")
django.setup()


from accounts.models import User
admin = User.objects.create_superuser('zanin.vowa2015@yandex.ru','hgakwlKAlcnMPae31ba','Vova')