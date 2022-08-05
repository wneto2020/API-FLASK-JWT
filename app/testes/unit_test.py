from flask import make_response
import unittest

from ..views import users

class TestApi(unittest.TestCase):
    def test_post_user(self):
        self.assertEqual(users.post_user("jaja", "123456"), ({"message": "Successfully registered"}, 201))

