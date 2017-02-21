from google.appengine.ext import ndb
from framework.request_handler import Mainhandlers


from hashlib import sha256
from base64 import b64encode
from os import urandom
import uuid
class AdminUsers(ndb.Model):
    UserName=ndb.StringProperty(required=True)
    AdminEmployee_id=ndb.StringProperty(required=True)
    AdminPhone=ndb.StringProperty(required=True)
    AdminEmail=ndb.StringProperty(required=True)
    AdminPassword=ndb.StringProperty(required=True)
    confirmation_code=ndb.StringProperty(required=False)
    confirmation_Mail=ndb.BooleanProperty(default=False)

    @classmethod
    def check_admin_email_if_exists(cls,AdminEmail):
        return cls.query(cls.AdminEmail == AdminEmail).get()
    @classmethod
    def add_admin_details(cls,UserName,AdminEmployee_id,AdminPhone,AdminEmail,AdminPassword):
        admin=cls.check_admin_email_if_exists(AdminEmail)
        if not admin:
            random_bytes=urandom(64)
            salt=b64encode(random_bytes).decode('utf-8')
            hashed_password=salt + sha256(salt + AdminPassword).hexdigest()

            confirmation_code=str(uuid.uuid4().get_hex())
            new_key_Admin=cls(
                UserName=UserName,
                AdminEmployee_id=AdminEmployee_id,
                AdminPhone=AdminPhone,
                AdminEmail=AdminEmail,
                AdminPassword=hashed_password,
                confirmation_code=confirmation_code

            ).put()
            return{
                'created':True,
                'AdminUser_ID':new_key_Admin.id(),
                'confirmation_code':confirmation_code
            }
        else:
            return {
                'created': False,
                'Message':'Email-ID Already exits.Try new Email-ID'
            }
    @classmethod
    def check_password(cls,email,password):
        user=cls.check_admin_email_if_exists(email)
        if user:
           hashed_password=user.AdminPassword
           salt=hashed_password[:88]
           check_password=salt+sha256(salt+password).hexdigest()
           if check_password==hashed_password:
               return user.key.id()
           else:
               return None
        else:
            return None