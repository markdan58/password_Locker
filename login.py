
#!/usr/bin/env python3.6

from  register import Register

def create_register(first_name,last_name,username,number,email,password,account_type):
    '''
    Function to create a new account
    '''
    new_register = Register (first_name,last_name,username,number,email,password,account_type)
    return new_register

def save_register(register):
    '''
    Function to save register
    '''
    register.save_register()

def del_register(register):
    '''
    Function to delete a register
    '''
    register.delete_register()

def find_register(number):
    '''
    Function that finds a contact by number and returns the register
    '''
    return Register.find_by_number(number)

    def check_existing_register(number):
    '''
    Function that check if account exists with that number and return a Boolean
    '''
    return Register.register_exist(number)

def display_register():
        '''
        Function that returns all the saved accounts
        '''
        return Register.display_register()

def main():
        print("Hello Welcome to your contact list. What is your name?")
        user_name = input()

        print(f"Hello {user_name}. what would you like to do?")
        print('\n')