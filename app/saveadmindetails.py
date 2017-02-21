from framework.request_handler import Mainhandlers
from models.datastoreadmin import AdminUsers
import re
from os import environ
from google.appengine.api import mail
class SaveAdminDetails(Mainhandlers):
    @classmethod
    def send_mail(cls,to,user_id,confirmation_code):
        email_object=mail.EmailMessage(
            sender='noreply@esanitation-control.appspotmail.com',
            subject='Confirm your mail to access the Admin Account',
            to=to
        )
        email_parameters={
            'domain':'http://localhost:8080' if environ['SERVER_SOFTWARE'].startswith('Development') else 'http://epsanitation-control.appspot.com',
            'user_id':user_id,
            'coonfirmation_code':confirmation_code
        }
        html_from_template=cls.jinja_environment.get_template('email/configuration_email.html').render(email_parameters)
        email_object.html=html_from_template
        email_object.send()

    def post(self):
        UserName=self.request.get('UserName')
        AdminEmployee_id=self.request.get('AdminEmployee_id')
        AdminPhone=self.request.get('AdminPhone')
        AdminEmail=self.request.get('AdminEmail')
        AdminPassword=self.request.get('AdminPassword')

        status=200
        if UserName and AdminEmployee_id and AdminPhone and AdminEmail and AdminPassword:
            email_validation="(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
            if re.match(email_validation,AdminEmail):
                admin_val=AdminUsers.add_admin_details(UserName=UserName,AdminEmployee_id=AdminEmployee_id,AdminPhone=AdminPhone,AdminEmail=AdminEmail,AdminPassword=AdminPassword)
                if admin_val['created']:
                    html=self.jinja_environment.get_or_select_template('comments/template_modal.html').render()
                    admin_json_response={
                        'html':html,
                    }
                    self.send_mail(to=AdminEmail,user_id=admin_val['AdminUser_ID'],confirmation_code=admin_val['confirmation_code'])
                else:
                    status=400
                    admin_json_response=admin_val
                self.json_response(status_code=status, **admin_json_response)
            else:
                status=400
                admin_json_response={
                    'Title': 'Error',
                    'Message': 'please Enter in correct email to continue.'
                }
                self.json_response(status_code=status, **admin_json_response)

        else:
            status = 400
            admin_json_response={

            }
            if not UserName:
                admin_json_response.update({
                    'Title':'Error',
                    'Message':'please fill in UserName to continue.'
                })
            if not AdminEmployee_id:
                admin_json_response.update({
                    'Title': 'Error',
                    'Message':'please fill in employee ID to continue.'
                })
            if not AdminPhone:
                admin_json_response.update({
                    'Title': 'Error',
                    'Message':'please fill in Phone No to continue.'
                })
            if not AdminEmail:
                admin_json_response.update({
                    'Title': 'Error',
                    'Message':'please fill in email to continue.'
                })
            if not AdminPassword:
                admin_json_response.update({
                    'Title': 'Error',
                    'Message':'please fill in password to continue.'
                })
            self.json_response(status_code=status,**admin_json_response)