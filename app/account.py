from framework.request_handler import Mainhandlers
from models.datastoreuser import Users

class UserAccount(Mainhandlers):
    @Mainhandlers.login_required
    def get(self):
        self.render('main.html')
    @Mainhandlers.login_required
    def post(self):
        user_key=self.check_user_logged_in.key
        toilet_id=self.request.get('toilet_id')
        employee_id=self.request.get('employee_id')
        location=self.request.get('location')

        Users.add_toilet_details(toilet_user_id=user_key,toilet_id=toilet_id,employee_id=employee_id,location=location)
        self.redirect('/save')