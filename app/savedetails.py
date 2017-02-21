from framework.request_handler import Mainhandlers
from models.datastoreuser import Users


class SaveDetails(Mainhandlers):
    def post(self):
        toilet_id=self.request.get('toilet_id')
        employee_id=self.request.get('employee_id')
        location=self.request.get('location')
        status = 200

        if toilet_id and employee_id and location:
            user_key = self.check_user_logged_in.key
            toilet_val= Users.add_toilet_details(toilet_user_id=user_key,toilet_id=toilet_id,employee_id=employee_id,location=location)
            if  toilet_val['created']:
                pass
            else:
                status=400
                json_response=toilet_val
                self.json_response(status_code=status, **json_response)

        else:
            status = 400
            json_response={

            }
            if not toilet_id:
                json_response.update({
                    'Title':'Error',
                    'Message':'please fill in toilet ID to continue.'
                })
            if not employee_id:
                json_response.update({
                    'Title': 'Error',
                    'Message':'please fill in employee ID to continue.'
                })
            self.json_response(status_code=status,**json_response)