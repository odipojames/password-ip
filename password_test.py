import unittest # importing the unittest module
import pyperclip
from password import User  #first import user c class

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

if __name__ == '__main__':
    unittest.main()