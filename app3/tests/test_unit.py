from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app


class TestBase(TestCase):
	def create_app(self):
		return app

class TestApiCalls(TestBase):
	def test_primeno(self):
		response = self.client.get('/primeno')
		self.assertIn(, response.data)