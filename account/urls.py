from django.urls import path, include
from . import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    path('api-jwt-auth', obtain_jwt_token),
    path('refresh_jwt_token', refresh_jwt_token),
    path('verify_jwt_token', verify_jwt_token),
    path('login', views.Signup),
]

#api-jwt-auth -> POST 방식으로 호출해야 jwt_token을 얻을 수 있다. 