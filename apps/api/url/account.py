import apps.api.views as rest_views
from django.urls import path, include
from rest_framework import routers

app_name = 'account'

router = routers.DefaultRouter()
router.register('signup', rest_views.SignupViewSet, basename='signup')  # 회원가입 api

urlpatterns = [
    path('', include(router.urls)),
]
