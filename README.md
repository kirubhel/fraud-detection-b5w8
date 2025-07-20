# B5W8: Fraud Detection for E-commerce and Banking - Interim 1

This project is part of the 10 Academy B5W8 challenge, aimed at improving detection of fraud cases using real-world bank and e-commerce transaction data.

## ✅ Tasks Completed (Interim 1)
- Data Cleaning (no missing or duplicate values)
- Merged IP addresses to countries using integer ranges
- Feature Engineering:
  - `time_since_signup`
  - `hour_of_day`, `day_of_week`
- Exploratory Data Analysis
- Class imbalance analysis (~9.36% fraud)
- Proposed oversampling/undersampling strategies

## 📁 Repository Structure

raud-detection-b5w8/
├── data/ # CSV files
├── notebooks/ # Jupyter Notebooks
│ └── 01_data_preprocessing_and_eda.ipynb
├── reports/ # Report PDFs
│ └── interim_1_report.pdf
├── requirements.txt
└── README.md


## 🛠️ Setup Instructions

```bash
git clone https://github.com/kirubhel/fraud-detection-b5w8.git
cd fraud-detection-b5w8
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook


📌 Submission Info
Author: Kirubel Gizaw

Challenge: B5W8 — Tenx Platform

Interim 1 Submission


---

#### 2. ✅ Move PDF into `reports/` Folder

In your terminal:
```bash
mv /mnt/data/interim_1_report.pdf reports/
