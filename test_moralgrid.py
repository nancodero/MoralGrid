# test_moralgrid.py
"""
Tests for MoralGrid module.
"""

import unittest
from moralgrid import MoralGrid

class TestMoralGrid(unittest.TestCase):
    """Test cases for MoralGrid class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MoralGrid()
        self.assertIsInstance(instance, MoralGrid)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MoralGrid()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
