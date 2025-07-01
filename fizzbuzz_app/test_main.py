import unittest
from unittest.mock import patch
from io import StringIO
import main

class TestMain(unittest.TestCase):
    @patch('builtins.input', return_value='35')
    @patch('sys.stdout', new_callable=StringIO)
    def test_output_fizzbuzz(self, mock_stdout, mock_input):
        main.main()
        self.assertIn("FIZZBUZZ", mock_stdout.getvalue())

if __name__ == "__main__":
    unittest.main()
