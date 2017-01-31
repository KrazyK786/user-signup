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

form = """
<h1>Signup</h1>
<label>Username:</label>
<label>Password:</label>
<label>Verify Password:</label>
<label>Email (optional):</label>
"""
def buildUser(user):
    user_label = "<label>Username:</label>"
    user_input = "<input type='text' name='username' /><br><br>"

    return user_label + user_input

def buildPassword(password, verify):
    pass_label = "<label>Password:</label>"
    pass_input = "<input type='text' name='password' /><br><br>"

    verify_label = "<label>Verify Password:</label>"
    verify_input = "<input type='text' name='verify' /><br><br>"

    return pass_label + pass_input + verify_label + verify_input

def buildEmail(email):
    email_label = "<label>Email (optional):</label>"
    email_input = "<input type='text' name='email' /><br><br>"

    return email_label + email_input

def buildPage(user,password,verify,email):

    header = "<h1>Signup</h1>"

    user_element = buildUser(user)

    password_element = buildPassword(password, verify)

    email_element = buildEmail(email)

    submit = "<input type='submit'/>"

    form = "<form method='post'>" + user_element + password_element + email_element + submit + "</form>"

    content = header + form

    return content





class MainHandler(webapp2.RequestHandler):
    def get(self):


        content = buildPage("","","","")
        self.response.write(content)

    def post(self):
        user = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")

        self.response.write(user + password + verify + email)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
