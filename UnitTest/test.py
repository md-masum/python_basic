import unittest
import main


class TestMain(unittest.TestCase):
    """Unit tests for the main module."""

    def setUp(self):
        """Set up any necessary variables or state before each test."""
        print("Setting up for test...")

    def test_do_stuff(self):
        """Test the do_stuff function with various inputs."""
        self.assertEqual(main.do_stuff(2), 4)
        self.assertEqual(main.do_stuff(3), 6)
        self.assertEqual(main.do_stuff(-1), -2)

    def test_do_stuff_with_zero(self):
        """Test the do_stuff function with zero."""
        self.assertEqual(main.do_stuff(0), 0)

    def test_do_stuff_with_string(self):
        """Test the do_stuff function with a string."""
        test_parameter = "string"
        result = main.do_stuff(test_parameter)
        self.assertIsInstance(result, ValueError, "Expected a value error for string input")

    def tearDown(self):
        """Clean up after each test."""
        print("Cleaning up after test...")




if __name__ == '__main__':
    unittest.main()
