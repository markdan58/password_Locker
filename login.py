
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