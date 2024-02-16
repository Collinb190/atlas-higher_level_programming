import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Class for testing the Rectanlge class."""

    def test_rectangle_init(self):
        # Test if Rectangle(1, 2) exists.
        r1 = Rectangle(1, 2)
        self.assertIsInstance(r1, Rectangle)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

        # Test if Rectangle(1, 2, 3) exists.
        r2 = Rectangle(1, 2, 3)
        self.assertIsInstance(r2, Rectangle)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)

        # Test if Rectangle(1, 2, 3, 4) exists.
        r3 = Rectangle(1, 2, 3, 4)
        self.assertIsInstance(r3, Rectangle)
        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)

        # Test if Rectanlge(1, 2, 3, 4, 5) exists.
        r4 = Rectangle(1, 2, 3, 4, 5)
        self.assertIsInstance(r4, Rectangle)
        self.assertEqual(r4.width, 1)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.x, 3)
        self.assertEqual(r4.y, 4)
        self.assertEqual(r4.id, 5)

    def test_rectangle_init_invalid_args(self):
        # Test if Rectangle("1", 2) exists.
        with self.assertRaises(TypeError):
            r = Rectangle("1", 2)

        # Test if Rectanlge(1, "2") exists.
        with self.assertRaises(TypeError):
            r = Rectangle(1, "2")

        # Test if Rectangle(1, 2, "3") exists.
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "3")

        # Test if Rectangle(1, 2, 3, "4") exists.
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, "4")

        # Test if Rectangle(-1, 2) exists.
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)

        # Test if Rectangle(1, -2) exists.
        with self.assertRaises(ValueError):
            r2 = Rectangle(1, -2)

        # Test if Rectanlge(0, 2) exists.
        with self.assertRaises(ValueError):
            r3 = Rectangle(0, 2)

        # Test if Rectangle(1, 0) exists.
        with self.assertRaises(ValueError):
            r4 = Rectangle(1, 0)

        # Test if Rectangle(1, 2, -3) exists.
        with self.assertRaises(ValueError):
            r5 = Rectangle(1, 2, -3)

        # Test if Rectangle(1, 2, 3, -4) exists.
        with self.assertRaises(ValueError):
            r6 = Rectangle(1, 2, 3, -4)

    def test_area_exists(self):
        # Test if the area() is available.
        r1 = Rectangle(1, 2)
        self.assertTrue(hasattr(r1, 'area'))

        r2 = Rectangle(3, 4)
        self.assertEqual(r2.area(), 12)

    def test_str(self):
        # Test if the __str__() exists.
        r1 = Rectangle(1, 2)
        self.assertTrue(hasattr(r1, '__str__'))

        # Test if the __str__() works
        r2 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r2), "[Rectangle] (5) 3/4 - 1/2")

    def test_display(self):
        # Test if display() without x and y exists.
        r1 = Rectangle(1, 2)
        self.assertTrue(hasattr(r1, 'display'))
        og_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            r1.display()
            display_output = sys.stdout.getvalue().strip()
            expected_output = "#\n#"
            self.assertEqual(display_output, expected_output)
        finally:
            sys.stdout = og_stdout

        # Test if display() without y exists.
        r2 = Rectangle(1, 2, 3, )
        self.assertTrue(hasattr(r2, 'display'))
        og_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            r2.display()
            display_output = sys.stdout.getvalue().strip()
            expected_output = "#\n   #"
            self.assertEqual(display_output, expected_output)
        finally:
            sys.stdout = og_stdout

        # Test if display() exists.
        r3 = Rectangle(1, 2, 3, 4)
        og_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            r3.display()
            display_output = sys.stdout.getvalue().strip()
            expected_output = "#\n   #"
            self.assertEqual(display_output, expected_output)
        finally:
            sys.stdout = og_stdout

    def test_to_dictionary(self):
        # Test if to_dictionary() exists.
        r1 = Rectangle(1, 2)
        self.assertTrue(hasattr(r1, 'to_dictionary'))

        # Test the out put of to_dictionary.
        r2 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r2.to_dictionary(), 
                        {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
                    )
