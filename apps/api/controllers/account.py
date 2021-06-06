from apps.api.controllers.controller import Controller
from rest_framework.response import Response


class SignupController(Controller):
    def run(self):  # viewset이 인자로 들어가는 부분
        # 비지니스 로직 작성
        return Response(self.response_message, status=self.status)
