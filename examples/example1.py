from UEQanalyzer.data_loader import load_ueq_data
from UEQanalyzer.analysis import calculate_mean_scores
from UEQanalyzer.visualization import plot_dimension_scores

# Load data
data = load_ueq_data("ueq_data.xlsx")

# Calculate mean scores
mean_scores = calculate_mean_scores(data)
print("Mean Scores:", mean_scores)

# Plot dimension scores
plot_dimension_scores(mean_scores)