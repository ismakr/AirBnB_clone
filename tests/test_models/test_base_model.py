#!/usr/bin/env python3
"""unittest module basemodel"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Define unittests for BaseModel"""

    def save_test(self):
        """test save method"""
        my_model = BaseModel()
        created_at = my_model.created_at
        updated_at = my_model.save()
        self.assertNotEqual(created_at, updated_at)


if __name__ == '__main__':
    unittest.main()
