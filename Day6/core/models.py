from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from core.models import Product


for user in User.objects.all():
    Token.objects.get_or_create(user=user)

content_type = ContentType.objects.get_for_model(Product)
permission = Permission.objects.create(
    codename='can_publish',
    name='Can Publish Posts',
    content_type=content_type,
)