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
