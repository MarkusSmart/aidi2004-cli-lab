import unittest
from app import greet, farewell

class TestApp(unittest.TestCase):

    def test_greet(self):
        result = greet("Alice")
        self.assertIn("Alice", result)

    def test_farewell(self):
        result = farewell("Bob")
        self.assertIn("Bob", result)

if __name__ == "__main__":
    unittest.main()
