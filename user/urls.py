from django.urls import path, include

from user.views import RegisterCreateAPIView

urlpatterns=[
    path('register/',RegisterCreateAPIView.as_view(),name='register'),
# path('captcha/', include('captcha.urls')),

]