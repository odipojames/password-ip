
import random
import string
import pyperclip

class User:
    '''
    a class that defines the name and password  of the user
    '''
    users_list = []


    def __init__(self,first_name,last_name,password):

        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):
        '''
        method that adds user into the user_list
        '''

        User.users_list.append(self)

class Credential:
    '''
    a class to create the create an account , save the passwords and sites then generate passwords
    '''
    creds_list =[]
    # user_creds_list=[]
    @classmethod
    def check_user(cls,first_name,password):
        '''
        method that checks if the name and password entered are in the system
        '''
        current_user = ''
        for user in User.users_list:
            if user.first_name == first_name and user.password == password:
                current_user = user.first_name
                return current_user

    def __init__(self,user_name,site_name,account_name,password):
        '''
        method that defines the properties of each credential object
        '''

        self.user_name = user_name
        self.site_name = site_name
        self.account_name = account_name
        self.password = password

    def save_credentials(self):
        '''
        method that saves credentials into the creds_list
        '''

        Credential.creds_list.append(self)

    def generate_password(size):
        '''
        function that generates a random password of length size
        '''
        a=string.printable
        pas_gen = ''.join(random.sample(a ,int(size)))
        return pas_gen

    @classmethod
    def display_creds(cls):
        '''
        method that returns the contents of the creds_list
        '''
        return  cls.creds_list

    @classmethod
    def find_site(cls,site_name):
        '''
        method that returns the credentials for the site that is searched for
        '''
        for cred in cls.creds_list:
            if cred.site_name == site_name:
                return cred
    @classmethod
    def copy_password(cls,site_name):
        pass_pick= Credential.find_site(site_name)
        return pyperclip.copy(pass_pick.password)
