from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import flask
from app import app


class TestBase(TestCase):
	def create_app(self):
		return app

class TestGenerate(TestBase):
	def test_generate(self):
		with patch ('requests.get') as s:
			s.return_value = "abcdefg"
			with patch ('requests.get') as p:
				p.return_value = "3"
				with patch ('requests.post') as sp:
					sp.return_value = "True"
					with patch ('requests.post') as pp:
						pp.return_value = "True"
						response = self.client.get('/home/generate')
						self.assertEqual(win, True)
