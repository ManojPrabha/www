#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

app = webapp2.WSGIApplication([
    webapp2.Route(r'/', handler='app.home.Home'),
    webapp2.Route(r'/new', handler='app.home.New'),
    webapp2.Route(r'/save', handler='app.savedetails.SaveDetails'),
    webapp2.Route(r'/saveadmin', handler='app.saveadmindetails.SaveAdminDetails'),
    webapp2.Route(r'/savestaff', handler='app.savestaffdetails.SaveStaffDetails'),
    webapp2.Route(r'/login', handler='app.login.LoginUser'),
    webapp2.Route(r'/account', handler='app.account.UserAccount')

], debug=True)
