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
import webapp2, cgi, re

page = """
<!DOCTYPE html>
    <head>
        <title>User-Signup</title>
        <style type= "text/css">
            .error {
                color: red;
            }
        </style>
    </head>
    <body>
    <h1>Signup</h1>
	<form method='post'>
		<label>Username: </label>
		<input type='text' name='username' value="%(username)s" required/>
		<span class='error'>%(username_error)s</span><br><br>

		<label>Password:</label>
		<input type='password' name='password' required/>
		<span class='error'>%(password_not_valid)s</span><br><br>

		<label>Verify Password:</label>
		<input type='password' name='verify' required/><br><br>
		<span class='error'>%(password_not_match)s</span>

		<label>Email (optional):</label>
		<input type='text' name='email' value="%(email)s"/>
		<span class='error'>%(email_error)s</span><br><br>

		<input type='submit'/>
	</form>
	</body>
"""

PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):

    return USER_RE.match(username)
def valid_password(password):
    return PASSWORD_RE.match(password)
def password_match(password,verify):
    return password == verify
def valid_email(email):
    return EMAIL_RE.match(email)

def valid_input(username,password,verify,email=""):
    valid_dic = {}
    if valid_username(username) is None:
        valid_dic["username_error"] = "That is not a valid username"
    if valid_password(password) is None:
        valid_dic["password_not_valid"] = "That is not a valid password"
    if password_match(password,verify) == False:
        valid_dic["password_not_match"] = "These passwords do not match"
    if email != "":
        if valid_email(email) is None:
            valid_dic["email_error"] = "This is not a valid email"

    return valid_dic



class MainHandler(webapp2.RequestHandler):
    def write_page(self,username_error="",password_not_valid="",password_not_match="",email_error="",username="",email=""):
        self.response.write(page % {"username_error":username_error,"password_not_valid":password_not_valid,"password_not_match":password_not_match,
                                    "email_error":email_error,"username":username,"email":email})

    def get(self):
        self.write_page()

    def post(self):
        user = self.request.get("username")
        pas = self.request.get("password")
        ver = self.request.get("verify")
        em = self.request.get("email")

        errors = valid_input(user,pas,ver,em)
        if len(errors) > 0:
            errors["username"] = user
            errors["email"] = em
            self.write_page(**errors)
        else:
            self.redirect("/welcome?username=" + user)

class Welcome(webapp2.RequestHandler):
    def get(self):
        user = self.request.get("username")
        self.response.write("<h1>Welcome, " + user + "!</h1>")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', Welcome)
], debug=True)
