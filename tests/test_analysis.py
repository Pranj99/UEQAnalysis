import unittest
import pandas as pd
from UEQanalyzer.analysis import calculate_mean_scores

class TestAnalysis(unittest.TestCase):
    def test_calculate_mean_scores(self):
        # Create a sample DataFrame
        data = pd.DataFrame({
            "Q1": [5, 6, 7],
            "Q2": [4, 5, 6],
            "Q3": [3, 4, 5],
            # Add more columns as needed
        })
        mean_scores = calculate_mean_scores(data)
        self.assertIsInstance(mean_scores, dict)
        self.assertIn("Attractiveness", mean_scores)