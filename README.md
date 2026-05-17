# E-commerce Customer Data Analysis

## Overview

This repository contains an exploratory data analysis project for e-commerce customer data. The goal is to inspect data quality, identify key customer behavior patterns, and provide a structured environment for data cleaning and reporting using a Jupyter notebook.

## Repository Structure

- `notebook.ipynb` - Primary analysis notebook for loading the dataset, performing data quality checks, and generating exploratory visualizations.
- `dataset/customer_data.csv` - Main customer dataset containing transactional and customer profile information.
- `dataset/ecommerce_customer_data_quality_practice.csv` - Supplemental dataset for practicing data quality validation and remediation techniques.

## Data Contents

The available datasets are intended to support analysis of customer behavior and data quality. Expected fields may include customer identifiers, demographic attributes, purchase history, and other relevant e-commerce fields.

### Key Data Focus

- Customer segmentation and profile completeness
- Purchase frequency and order behavior
- Data quality issues such as missing values, duplicates, and invalid entries
- Comparison of practice dataset quality with production-style data

## Getting Started

### Prerequisites

To work with this repository, you should have:

- Python 3.8+ installed
- A Jupyter environment or VS Code with the Jupyter extension
- Common data analysis libraries such as `pandas`, `numpy`, `matplotlib`, and `seaborn`

### Recommended Setup

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install pandas numpy matplotlib seaborn jupyter
```

### Running the Notebook

Open `notebook.ipynb` in a Jupyter environment or in VS Code and execute the notebook cells. The notebook is designed to:

1. Load both datasets from the `dataset/` folder
2. Inspect dataset structure and summary statistics
3. Identify data quality problems and missing values
4. Produce visualizations to support exploratory insights
5. Document observations and recommended next steps

## Analysis Workflow

The notebook generally covers the following steps:

1. Load and preview datasets
2. Check row and column counts
3. Validate data types and identify invalid formats
4. Detect duplicates and missing values
5. Visualize distribution of customer attributes and order activity
6. Summarize findings and propose data-cleaning actions

## Notes

- The dataset files are included in the `dataset/` folder and should remain together with the notebook for analysis to run correctly.
- If the notebook has cells that reference specific column names, verify that the column names in the CSV files match exactly.
- This repository is structured for learning data quality assessment and early-stage e-commerce customer analytics.

## License

This repository is provided for educational and practice purposes. No license is specified unless added explicitly.
