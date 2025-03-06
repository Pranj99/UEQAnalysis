import unittest
import pandas as pd
from UEQanalyzer.data_loader import load_ueq_data

class TestDataLoader(unittest.TestCase):
    def test_load_ueq_data(self):
        # Test loading a sample Excel file
        data = load_ueq_data("sample_data.xlsx")
        self.assertIsInstance(data, pd.DataFrame)
        self.assertFalse(data.empty)