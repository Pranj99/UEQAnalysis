# UEQanalyzer/analysis.py
import pandas as pd

def calculate_mean_scores(data):
    """
    Calculate the mean scores for each UEQ dimension (short version).

    Args:
        data (pd.DataFrame): DataFrame containing UEQ data.

    Returns:
        dict: A dictionary with mean scores for each dimension.
    """
    dimensions = {
        "Attractiveness": ["Q1", "Q2"],
        "Perspicuity": ["Q3", "Q4"],
        "Efficiency": ["Q5", "Q6"],
        "Dependability": ["Q7", "Q8"]
    }

    mean_scores = {}
    for dimension, questions in dimensions.items():
        mean_scores[dimension] = data[questions].mean(axis=1).mean()

    return mean_scores

def analyze_dimensions(data):
    """
    Perform a detailed analysis of UEQ dimensions (short version).

    Args:
        data (pd.DataFrame): DataFrame containing UEQ data.

    Returns:
        pd.DataFrame: A DataFrame with summary statistics for each dimension.
    """
    dimensions = {
        "Attractiveness": ["Q1", "Q2"],
        "Perspicuity": ["Q3", "Q4"],
        "Efficiency": ["Q5", "Q6"],
        "Dependability": ["Q7", "Q8"]
    }

    results = []
    for dimension, questions in dimensions.items():
        dimension_data = data[questions]
        results.append({
            "Dimension": dimension,
            "Mean": dimension_data.mean().mean(),
            "Median": dimension_data.median().median(),
            "Std Dev": dimension_data.std().mean()
        })

    return pd.DataFrame(results)