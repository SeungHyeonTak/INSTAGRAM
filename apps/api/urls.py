"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
import apps.api.views as rest_views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from rest_framework import routers

router = routers.DefaultRouter()
router.register('signup', rest_views.SignupViewSet, basename='signup')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', obtain_jwt_token),  # JWT 토큰을 발행할 때 사용
    path('api/token/verify/', verify_jwt_token),  # JWT 토큰이 유효한지 검증할 때 사용
    path('api/token/refresh/', refresh_jwt_token),  # JWT 토큰을 갱신할 때 사용
    path('', include(router.urls)),
    path('', include('apps.api.url.account', namespace='account'))
]

if settings.DEBUG:
    # django debug toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]
    # media file 서빙
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
