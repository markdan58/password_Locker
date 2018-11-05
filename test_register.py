import unittest # Importing the unittest module
from register import Register # Importing the Register class
import pyperclip


class TestRegister(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    # 1st Test is Testing if our objects are being initiated correctly
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_Register = Register("James","Muriuki","Jemo-Mruks","0712345678","james@ms.com","jMur463463","Instagram") # create register object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_Register.first_name,"James")
        self.assertEqual(self.new_Register.last_name,"Muriuki")
        self.assertEqual(self.new_Register.username,"Jemo-Mruks")
        self.assertEqual(self.new_Register.phone_number,"0712345678")
        self.assertEqual(self.new_Register.email,"james@ms.com")
        self.assertEqual(self.new_Register.password,"jMur463463")
        self.assertEqual(self.new_Register.account_type,"Instagram")


    # 2nd test is testing if our created register is saved
    def test_save_register(self):
        '''
        test_save_register test case to test if the register object is saved into
         the register list
        '''
        self.new_Register.save_register() # saving the new register
        self.assertEqual(len(Register.register_list),1)


    # 3rd testing if its saving multiple accounts
    def test_save_multiple_register(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_register.save_register()
            test_register = Register("Danmark","Masai","DMM","0790471962","danm@ms.com","ddmm454525","Twitter")# new register
            test_register.save_register()
            self.assertEqual(len(Register.register_list),2)


    # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Register.register_list = []

    # other test cases here
    def test_save_multiple_register(self):
            '''
            test_save_multiple_register to check if we can save multiple register
            objects to our register_list
            '''
            self.new_Register.save_register()
            test_register =  Register("Danmark","Masai","DMM","0790471962","danm@ms.com","ddmm454525","Twitter") # new register
            test_register.save_register()
            self.assertEqual(len(Register.register_list),2)
