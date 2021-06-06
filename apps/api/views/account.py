from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from apps.api.receivers.account import *
from apps.api.controllers.account import *
from apps.api.serializers.account import UserSerializer


class SignupViewSet(viewsets.ModelViewSet):
    """create 회원가입"""
    permission_classes = []
    authentication_classes = [JSONWebTokenAuthentication]

    serializer_class = UserSerializer
    metadata_class = ''

    def create(self, request, *args, **kwargs):
        receiver = None
        try:
            receiver = SignupReceiver(request)
            controller = SignupController(receiver)
            response = controller.run()
        except Exception as e:
            receiver.response_message = {'message': '서버 에러'}
            receiver.status = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = Response(receiver.response_message, status=receiver.status)

        return response
