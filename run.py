#!/usr/bin/env python3.6
from password import User , Credential

def create_profile(first_name,last_name,password):
    '''
    function to create a new user
    '''
    new_user = User(first_name,last_name,password)
    return new_user

def save_user(user):
    '''
    function that saves new users
    '''
    User.save_user(user)

def verify_profile(first_name,password):
    '''
    function that verifies the existance of a user before continuing to the credentials
    '''
    verify_user = Credential.check_user(first_name,password)
    return verify_user

def create_cred(user_name,site_name,account_name,password):
    '''
    function that creates cred(s) for the account and details the user wants to save
    '''
    new_cred = Credential(user_name,site_name,account_name,password)
    return new_cred

def save_cred(credential):
    '''
    function that saves new credentials
    '''
    Credential.save_credentials(credential)

def display_creds():
    '''
    function that returns the saved credentials
    '''
    return Credential.display_creds()

def generate_password(size):
    '''
    function to generate a password of length that is later to be specified
    '''
    return Credential.generate_password(size)

def copy_password(site_name):
    '''
    function that copys the password of a specified app onto a clipboard
    '''
    return Credential.copy_password(site_name)



def main():
    print (' ')
    print ('Welcome to My Password Locker App!')
    while True:
        print('*'*50)
        print('use the following short-codes to navigate: \n cp-create profile \n li-log in \n ex-exit')
        short_code = input('Enter short-code: ').lower().strip()
        if short_code == 'ex':
            break

        elif short_code == 'cp':
            print('-'*50)
            print(' ')
            print ('Fill in the following:')
            first_name = input('Enter your first name: ').strip()
            last_name = input('Enter your last name: ').strip()
            password = input('Enter password: ')
            save_user(create_profile(first_name,last_name,password))
            print (' ')
            print (f'new account created for:{first_name} {last_name} and password is {password} ')

        elif short_code == 'li':
            print ('-'*50)
            print(' ')
            print('Enter details:')
            user_name = input('Enter your first name: ').strip()
            password = str(input('Enter your password: '))
            user_exists = verify_profile(user_name,password)
            if user_exists == user_name:
                print (' ')
                # print ('waiting for more code')
                print (f'Welcome {user_name}.Now pick an option to continue')
                print (' ')
                while True:
                    print('-'*50)
                    print ('Nav-codes:\n cs-create site info \n ds-display site info \n cpy-copy password\n ex-exit')
                    nav_code = input('Enter Nav-code: ').strip().lower()
                    print('-'*50)
                    if nav_code == 'ex':
                        print(' ')
                        print(f'Goodbye{user_name}')
                        break
                    elif nav_code == 'cpy':
                        print(' ')
                        site = input('Enter the site name whose password you want to copy: ')
                        copy_password(site)
                        print(' ')
                    elif nav_code == 'cs':
                        print(' ')
                        print('Enter site details')
                        site_name = input('Enter the name of the site: ').strip()
                        account_name = input('Enter the account name: ').strip()
                        while True:
                            print(' ')
                            print('*'*50)
                            print('Pick an option for how you want to enter password:\n ep-enter current password \n gp-let app generate password for you \n ex-exit')
                            option = input('Enter an option: ').lower().strip()
                            print('-'*50)
                            if option == 'ep':
                                print(' ')
                                password = input('Enter your password: ')
                                break
                            elif option == 'gp':
                                size = int(input('How long should your password be: '))
                                password =generate_password(size)
                                break
                            elif option == 'ex':
                                break
                            else:
                                print('No such option! Try again')
                        save_cred(create_cred(user_name,site_name,account_name,password))
                        print(' ')
                        print (f'site information created for: {site_name} -Account name:{account_name} -Password:{password}')
                        print(' ')
                    elif nav_code == 'ds':
                        print(' ')
                        if display_creds():
                            print('here is a list of all your sites and their details')
                            print(' ')
                            for cred in display_creds():
                                print(f'Site name:{cred.site_name}.....Account name:{cred.account_name}.....Password:{password}')
                                print(' ')
                        else:
                            print(' ')
                            print('You dont seem to have any site and its details saved')
                            print(' ')


            else:
                print(' ')
                print('Wrong Details! Try again or create profile')
        else:
            print('*'*50)
            print(' ')
            print ('Sorry pick another option')

if __name__ == '__main__':
	main()
