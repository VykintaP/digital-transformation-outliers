# 🚀 Digital Transformation Outliers & Structural Shifts

* **Overview:**

  * Mirrors the complete Pandas + ML workflow from [Keith Galli’s course](https://www.youtube.com/watch?v=vmEHCJofslg), but applies it to real Eurostat data.
  * Replaces Pokémon with EU countries’ digital adoption and economic sector data.

* **Goals:**

  * Load & explore Eurostat ICT and GDP datasets.
  * Demonstrate Pandas fundamentals: reading files, filtering, sorting, conditional updates.
  * Group data by country or year to compute aggregates.
  * Scale multi-feature ICT data (Cloud, Broadband, E-sales, AI).
  * Use groupby to summarize by country or by time.
  * Create new calculated columns and reshape data.
  * Save cleaned datasets.

* **Methods & Tools:**

  * pandas for ETL, groupby, and manipulation
  * seaborn, matplotlib for plots
  * sklearn for scaling & later ML (PCA, clustering, outlier detection)

* **Project structure:**

  * notebooks/: Jupyter notebooks following step-by-step course exercises
  * scripts/: Python scripts for data cleaning & functions
  * docs/: Explanation notes & examples
  * reports/: Outputs like charts & CSV summaries
  * README.md: This overview

* **How to run:**

  * Clone the repo
  * Install packages (`pip install -r requirements.txt`)
  * Run notebooks in order: loading, cleaning, groupby summaries, scaling, basic plots.

* **Current status:**

  * [x] Project structure & plan drafted
  * [ ] Load Eurostat ICT dataset, explore rows, columns, cells
  * [ ] Filter & sort, conditional changes, create new columns
  * [ ] Groupby summaries & aggregate stats
  * [ ] Scale for future ML steps
  * [ ] Visualize trends & save outputs
