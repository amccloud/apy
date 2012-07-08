import unittest
from apy import Apy as _Apy
from apy import ApyValidationException
from apy.utils import *

class Apy(_Apy):
    def __request__(self, url, *args, **kwargs):
        return url, args, kwargs

class Zappos(Apy):
    __base_url__ = 'http://api.zappos.com/'

    def __toarg__(self, name):
        return underscore_to_camelcase(name, capfirst=True)

    def __tokwarg__(self, name):
        return underscore_to_camelcase(name, capfirst=False)

class ApyTestCase(unittest.TestCase):
    def test_instance(self):
        github = Apy('https://api.github.com/')

        results = github.users['amccloud'].repos()
        self.assertEqual(results[0], 'https://api.github.com/users/amccloud/repos')

        results = github('users', 'amccloud', 'repos')
        self.assertEqual(results[0], 'https://api.github.com/users/amccloud/repos')

    def test_custom_instance(self):
        zappos = Zappos()
        results = zappos.core_value('random')

        self.assertEqual(results[0], 'http://api.zappos.com/CoreValue/random')

    def test_instance_args(self):
        twitter = Apy('http://api.twitter.com/%s.json', 1)
        results = twitter.statuses.public_timeline()

        self.assertEqual(results[0], 'http://api.twitter.com/1/statuses/public_timeline.json')
        self.assertEqual(results[1], ('1', 'statuses', 'public_timeline'))

    def test_instance_kwargs(self):
        zappos = Zappos(key='YOUR_API_KEY')
        results = zappos.search(term='zombie')

        self.assertEqual(results[0], 'http://api.zappos.com/Search')
        self.assertEqual(results[2], {
            'key': 'YOUR_API_KEY',
            'term': 'zombie',
        })

    def test_validation(self):
        with self.assertRaises(ApyValidationException):
            zappos = _Apy('http://api.zappos.com/')
            zappos.search(term='zombie')
