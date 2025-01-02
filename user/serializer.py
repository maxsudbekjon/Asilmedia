from rest_framework.serializers import ModelSerializer,CharField,IntegerField,ValidationError
from captcha.fields import CaptchaField

from user.models import User


class RegisterModelSerializer(ModelSerializer):
    # captcha = CaptchaField()
    confirm_password=CharField(max_length=255)
    math=IntegerField()

    class Meta:
        model=User
        fields=['username','password','confirm_password','email','math']

