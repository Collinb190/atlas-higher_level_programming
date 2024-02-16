import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """This class is for testing the Base class."""
    def test_auto_assign_id(self):
        """Test if Base() assigns an ID automatically."""
        base_instance = Base()
        self.assertIsNotNone(base_instance.id)

    def test_auto_incremental_id(self):
        """Test if Base() assigns an ID + 1 of previous instance."""
        base_instance1 = Base()
        base_instance2 = Base()
        self.assertEqual(base_instance2.id, base_instance1.id + 1)

    def test_save_passed_id(self):
        """Test if Base(420) saves the passed ID."""
        base_instance = Base(420)
        self.assertEqual(base_instance.id, 420)

    def test_to_json_string_none(self):
        """Test if Base.to_json_string(None) is passed."""
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, '[]')

    def test_from_json_string_none(self):
        """Test if Base.from_json_string(None) is passed."""
        result = Base.from_json_string(None)
        self.assertEqual(result, [])
