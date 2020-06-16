from divide import divide
import unittest
from app import app


class TestDivide(unittest.TestCase):

    def test_div(self):
        res = divide(10, 2)
        self.assertEqual(res, 5)

    def setUp(self):
        self.app = app.test_client()

    #Testing any changes that have been made

    def test_no_parameters(self):
        response = self.app.get('/')
        assert response.data.decode("utf-8") == '{"error": true, "string": "Missing Parameters", "answer": 0}'

    def test_normal_modulo(self):
        response = self.app.get('/?x=12&y=5')
        assert response.data.decode("utf-8") == '{"error": false, "string": "12/5=2", "answer": 2}'

    def test_modulo_zero(self):
        response = self.app.get('/?x=12&y=0')
        assert response.data.decode("utf-8") == '{"error": true, "string": "Missing Parameters", "answer": 0}'

    def test_modulo_negative_by_negative(self):
        response = self.app.get('/?x=-12&y=-5')
        assert response.data.decode("utf-8") == '{"error": false, "string": "-12/-5=2", "answer": 2}'

    def test_modulo_negative_by_positive(self):
        response = self.app.get('/?x=-12&y=5')
        assert response.data.decode("utf-8") == '{"error": false, "string": "-12/5=-3", "answer": -3}'

    def test_modulo_positive_by_negative(self):
        response = self.app.get('/?x=12&y=-5')
        assert response.data.decode("utf-8") == '{"error": false, "string": "12/-5=-3", "answer": -3}'

    def test_non_int_param(self):
        response = self.app.get('/?x=3&y=apple')
        assert response.data.decode("utf-8") == '{"error": true, "string": "Missing Parameters", "answer": 0}'

    def test_missing_param(self):
        response = self.app.get('/?x=3')
        assert response.data.decode("utf-8") == '{"error": true, "string": "Missing Parameters", "answer": 0}'



if __name__ == '__main__':
    unittest.main()
