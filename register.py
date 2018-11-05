import pyperclip

class Register:
    """
    Class that generates new instances of register
    """

    register_list = [] # Empty register list


     # Init method up here
    def save_register(self):

        '''
        save_register method saves register objects into register_list
        '''

        Register.register_list.append(self)



    def __init__(self,first_name,last_name,username,number,email,password,account_type):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            first_name: New register first name.
            last_name : New register last name.
            username: New register Username
            number: New register phone number.
            email : New register email address.
            account_type : new register account_type.
        '''

         # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.phone_number = number
        self.email = email
        self.password = password
        self.account_type = account_type



    @classmethod
    def find_by_account_type(cls,account_type):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: acccount type to search for
        Returns :
            account that matches the account type.
        '''

        for register in cls.register_list:
            if register.account_type == account_type:
                return register



    @classmethod
    def register_exist(cls,account_type):
        '''
        Method that checks if a register exists from the contact list.
        Args:
            account_type: account_type to search if it exists
        Returns :
            Boolean: True or false depending if the account type exists
        '''
        for register in cls.register_list:
            if register.account_type == account_type:
                    return True

        return False



    @classmethod
    def display_register(cls):
        '''
        method that returns the account list
        '''
        return cls.register_list


    @classmethod
    def copy_email(cls,number):
        register_found = Register.find_by_number(number)
        pyperclip.copy(register_found.email)