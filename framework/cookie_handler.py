from hashlib import sha256


SECRET="Vtaa1Yj1bqXetimx0AISxZFOU32F34xC0K6rmgFZj2dEews/5/uyvgRPikDyZc7I2KAADI6aZ9yOnEjiu/is6g=="
def sign_cookie(value):
    string_value=str(value)
    signature=sha256(SECRET + string_value).hexdigest()
    return signature + "|" + string_value
def check_cookie(value):
    signature= value[:value.find('|')]
    declared_value= value[value.find('|')+1:]
    if sha256(SECRET + declared_value).hexdigest()==signature:
        return declared_value
    else:
        return None
