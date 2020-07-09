from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app


class TestBase(TestCase):
	def create_app(self):
		return app

class TestGenerate(TestBase):
	def test_generate(self):
		with patch ('requests.get') as s:
			s.return_value = "abcdefg"
			with patch ('request.get') as p:
				p.return_value = "3"
				with patch ('request.post') as sp:
					sp.return_value = "True"
					with patch ('request.post') as pp:
						pp.return_value = "True"
				response = self.client.get('/home/generate')
				self.assertIn(b'True', response.data)