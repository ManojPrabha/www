from google.appengine.ext import ndb
from google.appengine.api import search

class Users(ndb.Model):
    toilet_user_id=ndb.KeyProperty(kind='Users')
    toilet_id=ndb.StringProperty(required=True)
    employee_id=ndb.StringProperty(required=True)
    location=ndb.StringProperty(required=True)
    status=ndb.BooleanProperty()
    Alert_code=ndb.IntegerProperty()


    @classmethod
    def check_if_exists(cls,toilet_id):
        return cls.query(cls.toilet_id == toilet_id).get()
    @classmethod
    def add_toilet_details(cls,toilet_user_id,toilet_id,employee_id,location,status=True,Alert_code=0):
        stat=200
        print toilet_id,employee_id,location
        toilet = cls.check_if_exists(toilet_id)
        if not toilet:
            new_key=cls(
                toilet_id=toilet_id,
                employee_id=employee_id,
                location=location,
                status=True,
                Alert_code=0
            ).put()
            print new_key
            index = search.Index('toilets_search')
            doc = search.Document(
                doc_id=(str(new_key.id())),
                fields=[
                    search.TextField(name='toilet_user_id', value=toilet_user_id),
                    search.TextField(name='toilet_id', value=toilet_id),
                    search.TextField(name='employee_id', value=employee_id),
                    search.TextField(name='location', value=location),


                ]

            )
            index.put(doc)
            return dict(created=True, Toilet_ID=new_key.id())

        else:
            return {
                'created': False,
                'Message':'Toilet Already exits.Try new Toilet ID'
            }