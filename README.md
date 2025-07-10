Digital Transformation Outliers & Structural Shifts

* Overview:

  * Analyzes EU countries' adoption of digital technologies and structural economic changes over the past decade.
  * Uses unsupervised ML to detect outliers in ICT adoption.
  * Measures structural shifts with cosine distance on industry shares.

* Goals:

  * Identify outliers in digital adoption (e.g. cloud, broadband, e-sales, AI) vs GDP.
  * Compute how much each country’s economy changed from 2010 to 2023.
  * Visualize findings with scatter plots and radar charts.

* Methods & Tools:

  * pandas for cleaning & merging Eurostat data.
  * sklearn IsolationForest & OneClassSVM for anomaly detection.
  * scipy cosine distance for measuring changes.
  * seaborn, matplotlib, (optionally plotly) for visuals.

* Project structure:

  * notebooks/: Jupyter notebooks for EDA, ML, plotting
  * scripts/: Python scripts for ETL, metrics, visuals
  * docs/: Extended write-ups, summaries
  * reports/: Final charts & tables
  * README.md: Overview & instructions
  * .gitignore: Excludes data & large outputs

* How to run:

  * Clone the repo
  * Install packages (via requirements.txt or pip)
  * Run notebooks step by step to load data, fit models, compute distances, create plots.

* Current status:

  * [x] Initial structure & plan
  * [ ] Build data pipeline
  * [ ] Run ML models & cosine calculations
  * [ ] Produce final visuals & summary
