#!/usr/bin/env python3
"""unittest module basemodel"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class base_model(unittest.TestCase):
    """Define unittests for BaseModel"""

    def test_save_test(self):
        """test save method"""
        my_model = BaseModel()
        created_at = my_model.created_at
        updated_at = my_model.save()
        self.assertNotEqual(created_at, updated_at)

    def test_save_exit(self):
        """test if save exits"""
        self.assertEqual(hasattr(BaseModel, 'save'), True)

    def test_to_dict(self):
        """test to_dict method"""
        my_model = BaseModel()
        time = datetime.now()
        my_model.created_at = time
        my_model.updated_at = time
        my_model.id = "1010"
        dict_test = {
                'id': "1010",
                '__class__': "BaseModel",
                'created_at': time.isoformat(),
                'updated_at': time.isoformat()
        }
        self.assertDictEqual(my_model.to_dict(), dict_test)


if __name__ == '__main__':
    unittest.main()
