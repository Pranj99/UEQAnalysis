from UEQanalyzer.data_loader import load_ueq_data
from UEQanalyzer.analysis import calculate_mean_scores
from UEQanalyzer.analysis import analyze_dimensions
from UEQanalyzer.visualization import plot_dimension_scores, plot_item_means, plot_scale_means
from UEQanalyzer.analysis import transform_and_calculate_scales, calculate_item_statistics, calculate_scale_means

# Load data
data = load_ueq_data("ueq_data.xlsx")

# Calculate mean scores
mean_scores = calculate_mean_scores(data)
print("Mean Scores:", mean_scores)

transformed_data = transform_and_calculate_scales(data)
# Display the results
print(transformed_data)

# Plot dimension scores
plot_dimension_scores(mean_scores)

# Calculate item statistics
item_stats = calculate_item_statistics(transformed_data)
print("Item-wise Results:")
print(item_stats)

# Calculate scale means
scale_means = calculate_scale_means(transformed_data)
print("\nScale Means:")
print(scale_means)

# Plot item means
plot_item_means(item_stats)

# Plot scale means
plot_scale_means(scale_means)