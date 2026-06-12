# test_cryptochain.py
"""
Tests for CryptoChain module.
"""

import unittest
from cryptochain import CryptoChain

class TestCryptoChain(unittest.TestCase):
    """Test cases for CryptoChain class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoChain()
        self.assertIsInstance(instance, CryptoChain)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoChain()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
