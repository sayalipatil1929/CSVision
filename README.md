# 📊 CSVision – Dataset Health Checker (CLI Tool)
CSVision is a Python-based Command Line Interface (CLI) tool that automatically checks the health and quality of any CSV dataset.<br>
It helps data analysts quickly detect issues like missing values, duplicates, data type problems, and generates a clear health score with explanations before analysis begins.<br>
---
# 🚩 Problem Statement
Manual dataset validation is time-consuming and error-prone.<br>
Poor data quality often leads to incorrect insights and wasted analysis effort.
---
# ✅ Solution
CSVision automates dataset profiling and quality checks using Python, providing:<br>
* A health score (0–100)
* Human-readable explanations of issues
* Optional exportable reports
---
# 🧠 Project Workflow
* User provides a CSV file via CLI command
* Dataset is profiled (rows, columns, data types, missing values)
* Quality checks are applied (nulls, duplicates, invalid values)
* Health score is calculated based on rule-based scoring
* Explanations are generated for detected issues
* Final report is displayed or exported as a text file
![Workflow](https://github.com/sayalipatil1929/CSVision/blob/main/Workflow.png)
---
# 🛠 Tech Stack 
* Python
* Pandas
* CLI (argparse)
* CSV handling
* Modular Architecture.
---
# 📂 Project Structure
csvision/<br>
│<br>
├── cli.py              # Entry point (CLI command execution)<br>
├── profiler.py         # Dataset profiling logic<br>
├── checks.py           # Data quality checks<br>
├── scorer.py           # Health score calculation<br>
├── explainer.py        # Human-readable explanations<br>
├── __init__.py<br>
│<br>
├── sample.csv          # Sample dataset<br>
├── Superstore_csvision_report.txt  # Exported report<br>
├── README.md<br>
├── .gitignore<br>
---
# ▶️ How to Use
* Install Requirements
pip install pandas

* Run the Tool
`python csvision/cli.py your_dataset.csv`

* Export Report (Optional)
`python csvision/cli.py your_dataset.csv --export`

A report file will be generated automatically.
---
# 📁 Using Different Datasets
CSVision works with any CSV dataset, such as:<br>
* Sales data
* Financial data
* Survey results
* Customer or product data
* Academic or open datasets
* Just replace the file name:
`python csvision/cli.py new_data.csv`
---
# 📈 Output Includes
* Dataset size & structure
* Missing value analysis
* Duplicate detection
* Column-level issues
* Overall Health Score (0–100)
* Clear explanations of problems
---
# 🎯 Use Cases
* Data Analysts before EDA
* Data Cleaning validation
* Interview / portfolio project
* Data quality checks in pipelines
* Learning CLI-based Python tools
---
# ⭐ Key Highlights
* Modular and clean code structure
* Handles CSV encoding issues
* Fast and reusable for any dataset
* Beginner-friendly CLI design
---
# 🚀 Future Improvements
* Support for Excel & JSON files
* Visual dashboard integration
* Configurable scoring rules
* Automated data fixing suggestions
