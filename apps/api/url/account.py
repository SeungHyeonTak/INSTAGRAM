import apps.api.views as rest_views
from django.urls import path, include

app_name = 'account'

signup = rest_views.SignupViewSet.as_view({'post': 'create'})

urlpatterns = [
    path('account/authorization/signup/', signup, name='signup'),  # 회원가입 api
]
