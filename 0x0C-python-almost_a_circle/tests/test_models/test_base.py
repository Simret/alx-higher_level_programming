#!/usr/bin/python3
"""A Unittest for Base class"""
import unittest
from models.base import Base


class TestBaseclass(unittest.TestCase):
    """Test cases Base class"""
    def setUp(self):
        """Test raise heigt"""
        self.inst = Base(5)

    def tearDown(self):
         """Test raise heigt"""
         Base._Base__nb_objects = 0

    def test_nb_objs_yes(self):
        """Test raise heigt"""
        self.assertEqual(self.inst._Base__nb_objects, 0)

    def test_nb_objs_no(self):
        """Test raise heigt"""
        self.inst = Base()
        self.assertEqual(self.inst._Base__nb_objects, 1)

    def test_id(self):
        """Test raise heigt"""
        self.assertEqual(self.inst.id, 5)
