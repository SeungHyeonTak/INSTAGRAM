import apps.api.views as rest_view
from django.urls import path, include
from rest_framework import routers

app_name = 'account'

router = routers.DefaultRouter()
router.register('account/authorization/signup/', rest_view)  # 회원가입 api

urlpatterns = [
    path('', include(router.urls)),
]
