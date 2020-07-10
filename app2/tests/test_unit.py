from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app


class TestBase(TestCase):
	def create_app(self):
		return app

class TestApiCalls(TestBase):
	def test_letterstring(self):
		for i in range(20):
			response = self.client.get('/letterstring')
			self.assertIs(type(response.data.decode('utf-8')), str)