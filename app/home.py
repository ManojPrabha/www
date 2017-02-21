from framework.request_handler import Mainhandlers

class Home(Mainhandlers):
    def get(self):
        self.render('loginpage.html')
class New(Mainhandlers):
    def get(self):
        self.render('main.html')