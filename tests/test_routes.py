import unittest
from app import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_students(self):
        response = self.app.get("/students/")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()

