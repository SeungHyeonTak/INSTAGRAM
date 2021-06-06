from abc import ABC


class Controller(ABC):
    def __init__(self, receiver):
        self.__receiver = receiver
        self.__request = receiver.request

    @property
    def receiver(self):
        return self.__receiver

    @property
    def request(self):
        return self.__request

    @property
    def response_message(self):
        return self.receiver.response_message

    @response_message.setter
    def response_message(self, response_message):
        self.receiver.response_message = response_message

    @property
    def status(self):
        return self.receiver.status

    @status.setter
    def status(self, status):
        self.receiver.status = status
