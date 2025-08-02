# test_nextnexus.py
"""
Tests for NextNexus module.
"""

import unittest
from nextnexus import NextNexus

class TestNextNexus(unittest.TestCase):
    """Test cases for NextNexus class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NextNexus()
        self.assertIsInstance(instance, NextNexus)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NextNexus()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
