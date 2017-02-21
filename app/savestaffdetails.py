from framework.request_handler import Mainhandlers
from models.datastorestaff import StaffUser

class SaveStaffDetails(Mainhandlers):
    def post(self):
        EmployeeName=self.request.get('EmployeeName')
        Employeeid=self.request.get('Employee_id')
        EmployeePhone=self.request.get('EmployeePhone')
        EmployeeLocation=self.request.get('EmployeeLocation')

        status = 200

        if EmployeeName and Employeeid and EmployeePhone and EmployeeLocation:
            Emplolyee_val= StaffUser.add_staff_details(EmployeeName,Employeeid,EmployeePhone,EmployeeLocation)
            if  Emplolyee_val['created']:
                pass
            else:
                status=400
                json_response=Emplolyee_val
                self.json_response(status_code=status, **json_response)

        else:
            status = 400
            json_response={

            }
            if not EmployeeName:
                json_response.update({
                    'Title':'Error',
                    'Message':'please fill in Employee Name to continue.'
                })
            if not Employeeid:
                json_response.update({

                    'Title': 'Error',
                    'Message':'please fill in Employee ID to continue.'
                })
            if not EmployeePhone:
                json_response.update({

                    'Title': 'Error',
                    'Message': 'please fill in Employee Phone No to continue.'
                })
            if not EmployeeLocation:
                json_response.update({

                    'Title': 'Error',
                    'Message': 'please fill in Employee Location to continue.'
                })
            self.json_response(status_code=status,**json_response)