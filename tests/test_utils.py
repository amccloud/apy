import unittest
from apy.utils import *

class UtilsTestCase(unittest.TestCase):
    def test_camelcase_to_underscore(self):
        self.assertEqual(camelcase_to_underscore('testCaseString'), 'test_case_string')
        self.assertEqual(camelcase_to_underscore('TestCaseString'), 'test_case_string')
        self.assertEqual(camelcase_to_underscore('TESTCaseString'), 'test_case_string')
        self.assertEqual(camelcase_to_underscore('testCaseString', lower=False), 'test_Case_String')
        self.assertEqual(camelcase_to_underscore('TestCaseString', lower=False), 'Test_Case_String')

    def test_underscore_to_camelcase(self):
        self.assertEqual(underscore_to_camelcase('test_case_string'), 'testCaseString')
        self.assertEqual(underscore_to_camelcase('TEST_CASE_STRING'), 'testCaseString')
        self.assertEqual(underscore_to_camelcase('_test___case__string_'), 'testCaseString')
        self.assertEqual(underscore_to_camelcase('test_case_string', capfirst=True), 'TestCaseString')
        self.assertEqual(underscore_to_camelcase('test', capfirst=True), 'Test')

    def test_dot_to_underscore(self):
        self.assertEqual(dot_to_underscore('test.case.string'), 'test_case_string')
        self.assertEqual(dot_to_underscore('TEST.CASE.STRING'), 'test_case_string')
        self.assertEqual(dot_to_underscore('TEST.CASE.STRING', lower=False), 'TEST_CASE_STRING')
        self.assertEqual(dot_to_underscore('.test...case..string.'), 'test_case_string')

    def test_dot_to_camelcase(self):
        self.assertEqual(dot_to_camelcase('test.case.string'), 'testCaseString')
        self.assertEqual(dot_to_camelcase('TEST.CASE.STRING'), 'testCaseString')
        self.assertEqual(dot_to_camelcase('.test...case..string_'), 'testCaseString')
        self.assertEqual(dot_to_camelcase('test.case.string', capfirst=True), 'TestCaseString')
        self.assertEqual(dot_to_camelcase('test', capfirst=True), 'Test')
