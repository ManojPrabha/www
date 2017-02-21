from framework.request_handler import Mainhandlers
from models.datastoreadmin import AdminUsers

class LoginUser(Mainhandlers):
    def post(self):
        email=self.request.get('useremail')
        password=self.request.get('userpassword')
        user_id=AdminUsers.check_password(email,password)
        if user_id:
            self.send_cookie(name='User',value=user_id)
            self.redirect('/account')
        else:
            self.redirect('/')