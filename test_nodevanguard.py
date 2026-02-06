# test_nodevanguard.py
"""
Tests for nodeVanguard module.
"""

import unittest
from nodevanguard import nodeVanguard

class TestnodeVanguard(unittest.TestCase):
    """Test cases for nodeVanguard class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = nodeVanguard()
        self.assertIsInstance(instance, nodeVanguard)
        
    def test_run_method(self):
        """Test the run method."""
        instance = nodeVanguard()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
