from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app


class TestBase(TestCase):
	def create_app(self):
		return app

class TestApiCalls(TestBase):
	def test_checkstring(self):
		response = self.client.post('/checkstring', data='abcdefg')
		self.assertIn(b'True', response.data)

	def test_checkprime(self):
		response = self.client.post('/checkprime', data='3')
		self.assertIn(b'True', response.data)