#!/usr/bin/python3

from cromosoma.webmodel import WebModel
from cromosoma import corefields
from cromosoma.extrafields.emailfield import EmailField
from cromosoma.extrafields.passwordfield import PasswordField

class UserAdmin(WebModel):
    
    def create_fields(self):

        # I can change other fields here, how the name.

        self.register(corefields.CharField('username'))

        self.fields['username'].required=True

        self.register(corefields.CharField('password'))

        self.fields['password'].required=True

        self.register(EmailField('email'))

        self.fields['email'].required=True

        self.register(corefields.CharField('token_recovery'))

        self.register(corefields.BooleanField('privileges'))

"""

user_admin=WebModel('user_admin')

user_admin.register(corefields.CharField('username'))

user_admin.fields['username'].required=True

user_admin.register(corefields.CharField('password'))

user_admin.fields['password'].required=True

user_admin.register(EmailField('email'))

user_admin.fields['email'].required=True

user_admin.register(corefields.CharField('token_recovery'))

user_admin.register(corefields.BooleanField('privileges'))

#user_admin.register(corefields.CharField('prueba'))

"""