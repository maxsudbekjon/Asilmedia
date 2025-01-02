import random

from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User
from user.serializer import  RegisterModelSerializer

class Math:
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    jam = num1 + num2
@extend_schema(tags=['Register'],
               request=RegisterModelSerializer,
               responses=RegisterModelSerializer)
class RegisterCreateAPIView(APIView):
    def get(self,request):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        Math.num1 = num1
        Math.num2 = num2
        Math.jam = Math.num1 + Math.num2
        return Response(f'{Math.num1} + {Math.num2} = {Math.jam}?')

    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        confirm_password=request.data.get('confirm_password')
        email=request.data.get('email')
        math=request.data.get('math')
        if password!=confirm_password:
            raise ValidationError('Password not math')
        if math == Math.jam:
            raise ValidationError('Math is not jam')
        del request.data['confirm_password']
        del request.data['math']
        make_password(password)
        user=User.objects.create(username=username,password=password,email=email)
        user.save()
        return JsonResponse({'message':'Create'})






