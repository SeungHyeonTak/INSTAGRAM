from apps.api.receivers.receiver import Receiver


class SignupReceiver(Receiver):
    """회원가입 params 검사"""

    def __init__(self, request):
        super().__init__(request)
        self.email = None
        self.phone = None
        self.username = None
        self.fullname = None
        self.photo = None
        self.gender = None
        self.web_site = None
        self.introduction = None

    def set_params(self):
        self.email = self.request_data.get('email', None)
        self.phone = self.request_data.get('phone', None)
        self.username = self.request_data.get('username')
        self.fullname = self.request_data.get('fullname')
        self.photo = self.request_data.get('photo', None)
        self.gender = self.request_data.get('gender')
        self.web_site = self.request_data.get('web_site', None)
        self.introduction = self.request_data.get('introduction', None)

    def have_all_required_params(self):
        loss_params = []
        if not self.email and not self.phone:
            loss_params.append('email and phone')

        if not self.username:
            loss_params.append('username')

        if not self.fullname:
            loss_params.append('fullname')

        if loss_params:
            self.response_message = {
                'code': '000-000',
                'message': f'필수 파라미터({".".join(loss_params)}) 없음'
            }
            self.status = 400
            return False

        return True

    def is_valid_request(self):
        return self.have_all_required_params()
