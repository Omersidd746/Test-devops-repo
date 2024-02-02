# -*- coding: utf-8 -*-
from app import app

from flask.ext.testing import TestCase


class IndexTestCase(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_sum(self):
        self.assertEquals(2+2, 4)

    def test_index(self):
        rv = self.client.get('/')
        self.assert200(rv)

    def test_function_with_bug(self):
        result = my_buggy_function(5)  # Intentionally call a function with a bug
        assert result == 10, "Incorrect result returned"

    def test_function_with_bug():
        result = my_buggy_function(5)  # Intentionally call a function with a bug
        assert result == 10, "Incorrect result returned"

    def test_coding_standard_violation():
        with pytest.raises(SyntaxError):
            exec("x = 1  # Missing whitespace after #")  # Intentional syntax error
