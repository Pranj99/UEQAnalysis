"""
Example script for using the UEQanalyzer package.

This script demonstrates how to:
1. Load UEQ data from an Excel file.
2. Perform basic analysis (mean scores, item statistics, scale means).
3. Generate visualizations (dimension scores, item means, scale means with benchmarks).
4. Handle edge cases (missing data, invalid files).
5. Customize plots (titles, colors).

How to Run the Examples:
1. Ensure the `ueq_data.xlsx` file is in the same directory as this script.
2. Run the script using:
   ```bash
   python examples.py
3.Follow the printed instructions and view the generated plots.
"""

from UEQanalyzer.data_loader import load_ueq_data
from UEQanalyzer.analysis import (
calculate_mean_scores,
transform_and_calculate_scales,
calculate_item_statistics,
calculate_scale_means,
)
from UEQanalyzer.visualization import (
plot_dimension_scores,
plot_item_means,
plot_scale_means_with_benchmark,
)

def example_1_basic_usage():
# """Demonstrate basic usage of the package."""
    print("\n=== Example 1: Basic Usage ===")
    # Load data
    data = load_ueq_data("ueq_data.xlsx")
    if data is None:
        print("Failed to load data. Exiting.")
    
    # Transform data and calculate scales
    transformed_data = transform_and_calculate_scales(data)
    print("Transformed Data:")
    print(transformed_data.head())

    # Calculate mean scores of transformed data
    mean_scores = calculate_mean_scores(transformed_data)
    print("Mean Scores:")
    print(mean_scores)

    # Plot dimension scores
    plot_dimension_scores(mean_scores)

    # Calculate item statistics of transformed data
    item_stats = calculate_item_statistics(transformed_data)
    print("Item-wise Results:")
    print(item_stats)

    # Plot item means
    plot_item_means(item_stats)

    # Calculate scale means of transformed data
    scale_means = calculate_scale_means(transformed_data)
    print("Scale Means:")
    print(scale_means)

    # Plot scale means with benchmark
    plot_scale_means_with_benchmark(scale_means)
    return

def example_2_edge_cases():
    """Demonstrate handling edge cases."""
    print("\n=== Example 4: Edge Cases ===")
    # Example: Loading an invalid file
    print("Attempting to load an invalid file...")
    invalid_data = load_ueq_data("invalid_data.txt") #  a sample invalid file
    if invalid_data is None:
        print("Invalid data handled gracefully.")

    # Example: Handling missing data
    print("\nAttempting to load a file with missing data...")
    data_with_missing = load_ueq_data("ueq_data_missing.xlsx")  #  a sample file with missing data
    if data_with_missing is None:
        print("Supplied file has no data!")


if __name__ == "__main__":
# Run all examples
    example_1_basic_usage()
    example_2_edge_cases()

