import unittest # importing the unittest module
import pyperclip
from password import User,Credential  # import user and credential class

class TestUser(unittest.TestCase):
    '''
    a test class to run test cases on the behaviour of the user class
    '''

    # making the setup
    def setUp(self):
        '''
        what runs before each tet
        '''
        self.new_user = User("odipo","james","aoko122")

    def test_init_(self):
        '''
        testing whather objects is initialized correctly
        '''
        self.assertEqual(self.new_user.first_name,"odipo")
        self.assertEqual(self.new_user.last_name,"james")
        self.assertEqual(self.new_user.password,"aoko122")

    def test_save_user(self):
        '''
        test to check whether user information is being saved
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)

    def tearDown(self):
        '''
        cleans up after each test runs
        '''
        User.users_list = []


class TestCredentials(unittest.TestCase):
    '''
    a test class that tests the behaviours of the credentials class
    '''
    def test_confirm_user(self):
        '''
        a test to check whether the user that is trying to log in is a registered user
        '''
        self.new_user = User("odipo","james","aoko122")
        self.new_user.save_user()
        nwC=User("aaa","bbb","aoko122")
        nwC.save_user()

        for user in User.users_list:
            if user.first_name == nwC.first_name and user.password == nwC.password:
                current_user = user.first_name
                return current_user
                self.assertEqual(current_user,Credential.check_user(nwC.firts_name,nwC.password))

    def setUp(self):
        '''
        creates accounts before each test
        '''
        self.new_cred =Credential("odipo","fb","james","1234")

    def test_init_(self):
        '''
        test to check the creation of new user details
        '''
        self.assertEqual(self.new_cred.user_name,'odipo')
        self.assertEqual(self.new_cred.site_name,'fb')
        self.assertEqual(self.new_cred.account_name,'james')
        self.assertEqual(self.new_cred.password,'1234')

    def test_save_credentials(self):
        '''
        test to check if the new credentials are being saved into the creds_list
        '''
        self.new_cred.save_credentials()
        self.assertEqual(len(Credential.creds_list),1)

    def tearDown(self):
        '''
        function to clear creds_list before every test
        '''
        Credential.creds_list = []    

if __name__ == '__main__':
  unittest.main()
