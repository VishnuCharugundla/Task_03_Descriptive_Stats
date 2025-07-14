# 🗳️ Task 03: Descriptive Analysis of 2024 Election Ads

This project explores Facebook and Twitter political ads during the 2024 U.S. presidential election. Using **pure Python**, **Pandas**, and **Polars**, it computes identical summary statistics and generates visualizations to uncover trends in ad targeting, platform usage, topics, and call-to-action types.

---

## 🚀 How to Run

1. **Install dependencies**
   ```bash
   pip install pandas polars seaborn matplotlib
   ```

2. **Place data files** (CSV format) in the `period_03/` folder.
   > *Note: Data files are excluded from this repo.*

3. **Run scripts**
   * **Summary statistics** (produces identical results across all three approaches):
     ```bash
     python pure_python_stats.py
     python pandas_stats.py
     python polars_stats.py
     ```
   * **Visualizations**:
     ```bash
     python visualizations_script.py
     ```

4. **View outputs**
   * Statistics will be printed to console and/or saved as output files
   * Plots will be saved to the `plots/` directory

---

## 📊 Key Findings

### **Dataset Overview (246,745 ads analyzed)**
* **Top Advertisers**: "HARRIS FOR PRESIDENT" (49,788 ads) and "TRUMP 47 COMMITTEE"
* **Platform Dominance**: Facebook + Instagram were the primary ad platforms
* **Peak Activity**: October 27, 2024 saw 8,619 ads (highest single-day volume)
* **Spend Distribution**: Mean = $1,061, ranging from $49 to $474,999 (highly skewed)
* **Reach**: Average impressions = 45,601, with maximum of 1,000,000
* **Currency**: 99.9% of ads used USD
* **Unique Coverage**: 4,475 unique page IDs with all unique ad IDs

### **Statistical Analysis Results**
Each script successfully computed comprehensive descriptive statistics including:
- **Overall dataset statistics**: count, mean, min/max, standard deviation
- **Column-wise analysis**: unique value counts and most frequent values for categorical data
- **Aggregated analysis**: grouped by `page_id` and by `page_id` + `ad_id`
- **Topic & CTA Analysis**: Binary indicators (0-1 values) for fraud, incivility, governance, LGBTQ issues, etc.

---

## 🔬 Technical Comparison: Pure Python vs Pandas vs Polars

### **Output Consistency**
All three scripts successfully produced **identical numerical results**, demonstrating:
- **Pure Python**: Manual calculations using standard library functions
- **Pandas**: Built-in `.describe()`, `.value_counts()`, and `.groupby()` methods  
- **Polars**: Structured `.describe()` tables and efficient `.value_counts()` operations

### **Implementation Approaches**
- **Pure Python**: Required manual CSV parsing, custom statistical calculations, and explicit handling of data types and missing values
- **Pandas**: Leveraged comprehensive built-in statistical methods with intuitive syntax
- **Polars**: Modern syntax with optimized performance, especially for aggregation operations

### **Key Observations**
- **Data Handling**: Pure Python required significantly more code for basic operations like reading CSV and computing statistics
- **Performance**: Polars showed superior performance for large dataset operations and aggregations
- **Ease of Use**: Pandas provided the most straightforward approach for standard statistical analysis
- **Memory Efficiency**: Polars demonstrated better memory management for large datasets

### **Recommendation for Junior Analysts**
**Start with Pandas** for learning data analysis concepts due to:
- Extensive documentation and community support
- Intuitive method names and workflow  
- Wide industry adoption and job market relevance

**Consider Polars** for production work with larger datasets or performance-critical applications.

**Learn Pure Python** fundamentals to understand underlying statistical concepts and for environments with minimal dependencies.

---


## 📁 Repository Structure

```
Task_03_Descriptive_Stats/
├── pure_python_stats.py      # Base Python implementation
├── pandas_stats.py           # Pandas-based analysis  
├── polars_stats.py           # Polars-based analysis
├── visualizations_script.py  # Bonus visualizations
├── period_03/               # Data folder (excluded files)
├── plots/                   # Generated visualizations
└── README.md               # This file
```

## 📈 Time Series Analysis (New) - Task 04

A new notebook, `task04_summary.ipynb`, has been added to explore **temporal trends** in political ad data.

### 🔍 Objective
To visualize the relationship between the **daily number of ads** and **total spend over time** using Facebook’s 2024 U.S. presidential ad dataset.

### 📊 Visualization
The notebook introduces a dual-axis time series plot:
- **Blue Line** – Ad Count per day  
- **Red Dashed Line** – Total Spend per day (in $)

This plot highlights significant surges in political advertising activity and expenditure as the election approaches, reflecting campaign intensification in late 2023 and 2024.

<p align="center">
  <img src="plots/ad count and total spend over time.png" alt="Ad Count and Spend Over Time" width="700"/>
</p>

> ✅ This analysis uses **Pandas** and **Matplotlib**, showcasing how simple tools can uncover powerful temporal trends in political advertising.

### 📁 File
- [`task04_summary.ipynb`](task04_summary.ipynb)




*This analysis demonstrates the power of different Python approaches for statistical analysis, from foundational implementations to modern high-performance libraries.*
