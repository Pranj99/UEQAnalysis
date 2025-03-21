# UEQanalyzer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)

**UEQanalyzer** is a Python package for analyzing and visualizing data from the short version of **User Experience Questionnaire (UEQ)**. The UEQ is a fast and reliable questionnaire consisting of 8 questions designed to measure the user experience of interactive products. It covers a comprehensive impression of user experience, including both classical usability aspects (efficiency, perspicuity, dependability) and user experience aspects (originality, stimulation). 

This package provides tools to:
- Load and preprocess UEQ data.
- Calculate mean scores for UEQ dimensions.
- Transform and rescale data.
- Generate visualizations (e.g., dimension scores, item means, scale means with benchmarks).
- Handle edge cases (e.g., missing data, invalid files).

---

## Installation

You can install **UEQanalyzer** using `pip`:

```bash
pip install UEQanalyzer
```
Alternatively, you can install it directly from the source:
```bash
git clone https://github.com/Pranj99/UEQAnalysis.git
cd UEQAnalysis
pip install .
```
## Usage
Basic Usage
Here’s an example of how to use UEQanalyzer to analyze and visualize UEQ data:
```bash
from UEQanalyzer.data_loader import load_ueq_data
from UEQanalyzer.analysis import calculate_mean_scores, transform_and_calculate_scales
from UEQanalyzer.visualization import plot_dimension_scores

# Load data
data = load_ueq_data("ueq_data.xlsx")

# Transform the data from scale 1 to 7 to -3 to 3 
transformed_data = transform_and_calculate_scales(data)
```
Always transform data before calculating further statistics

```bash
# Calculate mean scores
mean_scores = calculate_mean_scores(transformed_data)

# Plot dimension scores
plot_dimension_scores(mean_scores)
```
## Examples
For more detailed examples, check out the examples/ directory in the repository. The examples demonstrate:

- Loading and preprocessing UEQ data.

- Calculating mean scores and item statistics.

- Comparing system results with benchmark
  
- Generating visualizations.

- Handling edge cases (e.g., invalid files, missing data).
## Command-Line Interface (CLI)

You can also use the UEQanalyzer CLI to analyze and visualize UEQ data:

**Basic Usage**

To analyze UEQ data and display results in the terminal:
```bash
ueqanalyzer -i ueq_data.xlsx
```
**Save Results to a CSV File**

To save the analysis results to a CSV file:
```bash
ueqanalyzer -i ueq_data.xlsx -o results.csv
```
**Generate and Display Plots**

To generate and display plots for UEQ dimensions, item means, and scale means:
```bash
ueqanalyzer -i ueq_data.xlsx -p
```
**Save Results and Generate Plots**

To save the results to a CSV file and generate plots:
```bash
ueqanalyzer -i ueq_data.xlsx -o results.csv -p
```

- -i or --input: Path to the input Excel file containing UEQ data.

- o or --output: Path to save the analysis results (optional).

- p or --plot: Generate and display plots for UEQ dimensions.

## Limitations

While UEQanalyzer is designed to be robust, there are some limitations to keep in mind:

- **Data Format:**

The input Excel file must contain exactly 8 questions (Q1 to Q8).

The scale for each question must be in the range of 1 to 7.

Missing or incomplete data is not supported. Ensure all questions are answered by users.

- **Data Collection:**

Currently, the package assumes data is collected via Google Forms or similar tools that enforce complete responses.

If your data collection method allows missing responses, you will need to preprocess the data before using this package.

