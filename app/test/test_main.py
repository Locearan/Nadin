import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app
class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    def test_hello_endpoint(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello, World", response.data)
    def test_heavy_endpoint(self):
        response = self.app.get('/heavy')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Heavy task completed", response.data)
    def test_metrics_endpoint(self):
        response = self.app.get('/metrics')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"app_request_count_total", response.data)
if __name__ == '__main__':
    unittest.main()