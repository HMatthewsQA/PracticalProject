from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import flask
from app import app


class TestBase(TestCase):
	def create_app(self):
		return app

class Testhome(TestBase):
	def test_homepage_view(self):
		response = self.client.get(url_for('home'))
		self.assertEqual(response.status_code, 200)

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
						self.assertEqual(response.win, True)


