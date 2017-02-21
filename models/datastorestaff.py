from google.appengine.ext import ndb
from framework.request_handler import Mainhandlers

from hashlib import sha256
from base64 import b64encode
from os import urandom
import uuid
class StaffUser(ndb.Model):
    EmployeeName=ndb.StringProperty(required=True)
    Employee_id=ndb.StringProperty(required=True)
    EmployeePhone=ndb.StringProperty(required=True)
    EmployeeLocation=ndb.StringProperty(required=True)


    @classmethod
    def check_employee_if_exists(cls,Employee_id):
        return cls.query(cls.Employee_id == Employee_id).get()
    @classmethod
    def add_staff_details(cls,EmployeeName,Employee_id,EmployeePhone,EmployeeLocation):
        stat=200
        staff = cls.check_employee_if_exists(Employee_id)
        if not staff:
            new_key_staff=cls(
                EmployeeName=EmployeeName,
                Employee_id=Employee_id,
                EmployeePhone=EmployeePhone,
                EmployeeLocation=EmployeeLocation,
            ).put()
            print new_key_staff
            return dict(created=True, Staff_ID=new_key_staff.id())
        else:
            return {
                'created': False,
                'Message':'Staff Already exits.Try new Employee ID'
            }