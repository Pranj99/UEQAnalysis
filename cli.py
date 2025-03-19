import argparse
from UEQanalyzer.data_loader import load_ueq_data
from UEQanalyzer.analysis import calculate_mean_scores, analyze_dimensions
from UEQanalyzer.visualization import plot_dimension_scores

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="UEQ Analysis Tool: Analyze and visualize UEQ data.")

    # Add arguments
    parser.add_argument(
        "-i", "--input",
        required=True,
        help="Path to the input Excel file containing UEQ data."
    )
    parser.add_argument(
        "-o", "--output",
        help="Path to save the analysis results (optional)."
    )
    parser.add_argument(
        "-p", "--plot",
        action="store_true",
        help="Generate and display plots for UEQ dimensions."
    )

    # Parse arguments
    args = parser.parse_args()

    # Load data
    print(f"Loading data from {args.input}...")
    data = load_ueq_data(args.input)
    if data is None:
        print("Failed to load data. Exiting.")
        return

    # Perform analysis
    print("Calculating mean scores for UEQ dimensions...")
    mean_scores = calculate_mean_scores(data)
    print("Mean Scores:")
    for dimension, score in mean_scores.items():
        print(f"{dimension}: {score:.2f}")

    # Save results (if output path is provided)
    if args.output:
        results = analyze_dimensions(data)
        results.to_csv(args.output, index=False)
        print(f"Analysis results saved to {args.output}.")

    # Generate plots (if --plot is specified)
    if args.plot:
        print("Generating plots...")
        plot_dimension_scores(mean_scores)

if __name__ == "__main__":
    main()