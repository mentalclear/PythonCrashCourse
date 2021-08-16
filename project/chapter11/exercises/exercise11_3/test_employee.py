import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """ Tests for the class Employee """

    def setUp(self):
        """ Create an instance of an emplyee """
        self.emplyee = Employee('Tedd', 'Tess', 80000) 

    def test_give_default_raise(self):
        self.emplyee.give_raise()
        self.assertEquals(self.emplyee.salary, 85000)

    def test_give_custom_raise(self): 
        self.emplyee.give_raise(10000)
        self.assertEquals(self.emplyee.salary, 90000)



if __name__ == '__main__':
    unittest.main()