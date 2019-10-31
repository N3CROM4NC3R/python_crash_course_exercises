import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee("santiago","padron",400000)

    def test_give_default_raise(self):
        """ With a raise of 5000,default """
        self.annual_salary = self.employee.annual_salary
        self.assertEqual(self.employee.give_raise(),self.annual_salary+5000)

    def test_give_custom_raise(self):
        """ With a raise of 10000,not default """
        self.annual_salary = self.employee.annual_salary
        self.annual_salary += 10000
        self.assertEqual(self.employee.give_raise(10000),self.annual_salary)