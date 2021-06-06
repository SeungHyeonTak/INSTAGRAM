from abc import ABC, abstractmethod
from rest_framework import status as status_code
from rest_framework.reverse import reverse


class Receiver(ABC):
    """
    view에서 들어오는 request를 검사하는 class
    view에서 들어오는 request를 받아서 controller에서 쓰일 인자 추출
    추출한 인자들을 검사해 필수 인자가 빠진지 검사
    """

    def __init__(self, request):
        self.__request = request
        self.__request_data = request.query_params if request.method == 'GET' else request.data
        self.__status = status_code.HTTP_200_OK
        self.__user = request.user
        self.__response_message = {}

    @property
    def request(self):
        return self.__request

    @property
    def request_data(self):
        """
        request에 전달된 params를 가지고 온다.
        GET - Query String
        POST - body
        """
        return self.__request_data

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def user(self):
        return self.__user

    @property
    def response_message(self):
        return self.__response_message

    @response_message.setter
    def response_message(self, response_message):
        self.__response_message = response_message

    # 파라미터 검사
    def is_valid_request(self):
        self.set_params()
        return self.have_all_required_params()

    @abstractmethod
    def set_params(self):
        """클라이언트에서 보낸 파라미터를 받는 함수."""
        pass

    @abstractmethod
    def have_all_required_params(self):
        """클라이언트에서 보낸 데이터가 필수 파라미터들을 전부 담고 있는지 확인하는 함수"""
        pass
