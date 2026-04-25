# 🎮 Video Game Sales Analysis & Dashboard (DVA Project)

This repository contains the data analysis, cleaning pipeline, exploratory data analysis (EDA), and Tableau dashboard visualizations for the **Video Game Sales** dataset. This project aims to uncover industry trends, regional market distributions, and the correlation between critic/user scores and global sales.

## 👥 Team Members (SecE_G15)
- Param Khodiyar
- Mayank Pillai
- Aaditya Yadav
- Sarabjeet Singh
- Anuj Upadhyay
- Ankita Thakur

## 📁 Project Structure

*   **`data/`**: Contains raw and processed datasets.
    *   `raw/`: The original uncleaned video game sales dataset.
    *   `processed/`: Cleaned dataset (`video_games_cleaned.csv`) and various pre-aggregated KPI files (e.g., `genre_kpi.csv`, `platform_kpi.csv`, `year_kpi.csv`) generated for Tableau.
*   **`notebooks/`**: Jupyter notebooks for data processing and analysis.
    *   `02_cleaning.ipynb`: ETL pipeline for handling missing values and feature engineering (Era, Score Gap, etc.).
    *   `03_eda.ipynb`: Exploratory Data Analysis highlighting global trends, top games, and correlations.
    *   `04_statistical_analysis.ipynb`: In-depth statistical testing and findings.
    *   `05_final_data_for_tableau.ipynb`: Generates the aggregated KPI CSVs used in the Tableau dashboard.
*   **`docs/`**: Project documentation.
    *   Contains guides such as `additional_charts_guide.md` and `tableau_dashboard_guide.md` which provide step-by-step instructions for rebuilding the Tableau dashboards.
*   **`scripts/`**: Python scripts for automation.
    *   `generate_additional_kpis.py`: Script to generate further KPI cuts from the cleaned dataset.
*   **`tableau/`**: Contains the final exported `.twbx` (Tableau Packaged Workbooks) and dashboard screenshots.
*   **`reports/`**: Final project reports and presentations.

## 📊 Tableau Dashboard Overview

The interactive Tableau dashboard consists of three main pages:

1.  **Executive Overview**: High-level market snapshot including total sales, total games, peak sales years, top 10 best-selling games, and regional sales distribution.
2.  **Genre & Platform Deep Dive**: Comparative analysis showing revenue generation by genre and platform, and how genre popularity evolved across different eras.
3.  **Regional & Ratings Analysis**: Explores correlations between critic scores and sales, the "Score Gap" between critics and users, and regional sales breakdowns.

### How to use the Dashboard:
1.  Open the packaged workbook located in the `tableau/` folder using **Tableau Desktop** or **Tableau Public**.

## 🚀 Getting Started

To run the data processing pipeline locally:

1.  Ensure you have Python 3 and Jupyter Notebook installed.
2.  Install required dependencies (pandas, matplotlib, seaborn, etc.).
3.  Execute the notebooks in order (02 -> 03 -> 04 -> 05) to generate the final cleaned data and KPIs.
