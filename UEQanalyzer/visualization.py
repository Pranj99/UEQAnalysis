import matplotlib.pyplot as plt
import pandas as pd

def plot_dimension_scores(mean_scores):
    """
    Plot the mean scores for each UEQ dimension.

    Args:
        mean_scores (dict): A dictionary with mean scores for each dimension.
    """
    dimensions = list(mean_scores.keys())
    scores = list(mean_scores.values())

    plt.figure(figsize=(10, 6))
    plt.bar(dimensions, scores, color="skyblue")
    plt.xlabel("UEQ Dimensions")
    plt.ylabel("Mean Score")
    plt.title("Mean Scores for UEQ Dimensions")
    plt.ylim(1, 7)  # UEQ scores range from 1 to 7
    plt.show()