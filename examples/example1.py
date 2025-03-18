from UEQanalyzer.data_loader import load_ueq_data
from UEQanalyzer.analysis import analyze_dimensions
from UEQanalyzer.visualization import plot_dimension_scores, plot_item_means, plot_scale_means, plot_scale_means_with_benchmark
from UEQanalyzer.analysis import transform_and_calculate_scales, calculate_item_statistics, calculate_scale_means, calculate_mean_scores

# Load data
data = load_ueq_data("ueq_data.xlsx")

# Calculate mean scores
# mean_scores = calculate_mean_scores(data)
# print("Mean Scores:", mean_scores)

transformed_data = transform_and_calculate_scales(data)
# Display the results
print(transformed_data)

# Calculate mean scores
mean_scores = calculate_mean_scores(transformed_data)
print("Mean Scores:")
print(mean_scores)

# Plot dimension scores
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

plot_scale_means_with_benchmark(scale_means)