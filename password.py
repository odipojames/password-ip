import random
import string
import pyperclip

class User:
    '''
    a class that defines the name(s) and password  of the user
    '''
    users_list = []


    def __init__(self,first_name,last_name,password):

        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):
        '''
        method that adds user(s) into the user_list
        '''
    def save_user(self):
        '''
        method that adds user(s) into the user_list
        '''

        User.users_list.append(self)
    