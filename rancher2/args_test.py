import unittest
import argparse

import rancher2.args as rancher2_args

class Rancher2_V3API_Args_Test(unittest.TestCase):
    """Tests for `args.py`."""

    def test_args(self):
        """Test creating an arguments object"""
        args = rancher2_args.Rancher2_V3API_Args()
        self.assertTrue(args.parse(['get', '--api-url', 'test', '--api-token', 'test']))
        self.assertIsInstance(args.get_collection(), tuple)

if __name__ == '__main__':
    unittest.main()
