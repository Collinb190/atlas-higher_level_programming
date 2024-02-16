import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Class for testing square class."""

    def test_square_init(self):
        # Test if Square(1) exists.
        s1 = Square(1)
        self.assertIsInstance(s1, Square)
        self.assertEqual(s1.width, 1)

        # Test if Square(1, 2) exists.
        s2 = Square(1, 2)
        self.assertIsInstance(s2, Square)
        self.assertEqual(s2.width, 1)
        self.assertEqual(s2.x, 2)

        # Test if Square(1, 2, 3) exists.
        s3 = Square(1, 2, 3)
        self.assertIsInstance(s3, Square)
        self.assertEqual(s3.width, 1)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 3)
