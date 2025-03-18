import matplotlib.pyplot as plt
import pandas as pd

def plot_dimension_scores(mean_scores):
    """
    Plot the mean scores for each UEQ dimension.
    """
    dimensions = list(mean_scores.keys())
    scores = list(mean_scores.values())

    plt.figure(figsize=(10, 6))
    plt.bar(dimensions, scores, color="skyblue")
    plt.xlabel("UEQ Dimensions")
    plt.ylabel("Mean Score")
    plt.title("Mean Scores for UEQ Dimensions")
    plt.ylim(-3, 3)  # UEQ scores range from 1 to 7
    plt.show()

def plot_item_means(item_stats):
    """
    Plot the mean value per item.
    """
    colors = ['blue' if i < 4 else 'red' for i in range(len(item_stats))]
    plt.figure(figsize=(10, 6))
    plt.bar(item_stats['Item'], item_stats['Mean'], color=colors)
    plt.xlabel('Item')
    plt.ylabel('Mean Value')
    plt.title('Mean Value per Item')
    # plt.axhline(y=0.8, color='green', linestyle='--', label='Positive Threshold (0.8)')
    # plt.axhline(y=-0.8, color='red', linestyle='--', label='Negative Threshold (-0.8)')
    plt.ylim(-3, 3)
    plt.legend()
    plt.show()

def plot_scale_means(scale_means):
    """
    Plot the mean value for Short UEQ Scales.
    """
    plt.figure(figsize=(8, 5))
    plt.bar(scale_means['Scale'], scale_means['Mean'], color='lightgreen')
    plt.xlabel('Scale')
    plt.ylabel('Mean Value')
    plt.title('Short UEQ Scales')
    # plt.axhline(y=0.8, color='green', linestyle='--', label='Positive Threshold (0.8)')
    # plt.axhline(y=-0.8, color='red', linestyle='--', label='Negative Threshold (-0.8)')
    plt.ylim(-3, 3)
    plt.legend()
    plt.show()