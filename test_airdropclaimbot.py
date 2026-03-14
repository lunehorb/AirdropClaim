# test_airdropclaimbot.py
"""
Tests for AirdropClaimBot module.
"""

import unittest
from airdropclaimbot import AirdropClaimBot

class TestAirdropClaimBot(unittest.TestCase):
    """Test cases for AirdropClaimBot class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AirdropClaimBot()
        self.assertIsInstance(instance, AirdropClaimBot)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AirdropClaimBot()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
