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

        while True:
                print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

                short_code = input().lower()

                if short_code == 'cc':
                        print("New account")
                        print("-"*10)

                        print ("First name ....")
                        f_name = input()

                        print("Last name ...")
                        l_name = input()

                        print("username ...")
                        p_number = input()

                        print("Phone number ...")
                        p_number = input()

                        print("Email address ...")
                        e_address = input()

                        print("password ...")
                        password = input()

                        print("account_type ...")
                        account_type = input()


                        save_register(create_register(f_name,l_name,user_name,p_number,e_address,password,account_type)) # create and save new account.
                        print ('\n')
                        print(f"New account {f_name} {l_name} created")
                        print ('\n')

                elif short_code == 'dc':

                        if display_register():
                                print("Here is a list of all your accounts")
                                print('\n')

                                for register in display_register():
                                        print(f"{register.first_name} {register.last_name} .....{register.phone_number}")

                                print('\n')
                        else:
                                print('\n')
                                print("You dont seem to have any accounts saved yet")
                                print('\n')

                elif short_code == 'fc':

                        print("Enter the number you want to search for")

                        search_number = input()
                        if check_existing_register(search_number):
                                search_register = find_register(search_number)
                                print(f"{search_register.first_name} {search_register.last_name}")
                                print('-' * 20)

                                print(f"Phone number.......{search_register.phone_number}")
                                print(f"Email address.......{search_register.email}")
                        else:
                                print("That account does not exist")

                elif short_code == "ex":
                        print("Bye .......")
                        break
                else:
                        print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
      main()

