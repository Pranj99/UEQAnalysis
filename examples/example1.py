"""
Example script for using the UEQanalyzer package.

This script demonstrates how to:
1. Load UEQ data from an Excel file.
2. Perform basic analysis (mean scores, item statistics, scale means).
3. Generate visualizations (dimension scores, item means, scale means with benchmarks).

How to Run the Examples:
1. Ensure the `ueq_data.xlsx` file is in the same directory as this script.
2. Follow the printed instructions and view the generated plots.
"""
from UEQanalyzer.data_loader import load_ueq_data
from UEQanalyzer.visualization import plot_dimension_scores, plot_item_means, plot_scale_means, plot_scale_means_with_benchmark
from UEQanalyzer.analysis import transform_and_calculate_scales, calculate_item_statistics, calculate_scale_means, calculate_mean_scores

# Load data
data = load_ueq_data("ueq_data.xlsx")

# Transform the data from scale 1 to 7 to -3 to 3 
transformed_data = transform_and_calculate_scales(data)
print(transformed_data)

# Calculate mean scores
mean_scores = calculate_mean_scores(transformed_data)
print("Mean Scores:") 
print(mean_scores)

# Plot mean scores
plot_dimension_scores(mean_scores)

# Calculate item statistics
item_stats = calculate_item_statistics(transformed_data)
print("Item-wise Results:")
print(item_stats)

# Plot item means
plot_item_means(item_stats)

# Calculate scale means
scale_means = calculate_scale_means(transformed_data)
print("\nScale Means:")
print(scale_means)

# Plot scale means
plot_scale_means(scale_means)

# Plot benchmark
plot_scale_means_with_benchmark(scale_means)