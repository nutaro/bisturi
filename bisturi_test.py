import unittest
import sys
from bisturi import scan
from unittest.mock import MagicMock, patch, create_autospec


class MyTestCase(unittest.TestCase):

    def test_generate_range(self):
        with patch('subprocess.Popen') as call_mock:
            scan('192.168.15.0/24', ['-a', '-v'])
            self.assertTrue(call_mock.called)


if __name__ == '__main__':
    unittest.main()
