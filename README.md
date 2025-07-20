# B5W8: Improved Detection of Fraud Cases (Interim 1)

This project addresses the challenge of detecting fraudulent transactions in e-commerce and bank transaction data, as part of the 10 Academy Week 8 challenge.

## 👨‍💻 Project Description

We explore and analyze two types of data:
- **E-commerce fraud transactions** (`Fraud_Data.csv`)
- **Credit card fraud transactions** (`creditcard.csv`)
- **Geolocation mapping** via IP address (`IpAddress_to_Country.csv`)

Our goal in Interim 1 is to prepare the data and engineer meaningful features that can aid in fraud detection.

## 📂 Directory Structure

fraud-detection-b5w8/
├── data/ # Raw datasets
├── notebooks/ # Jupyter Notebooks
├── reports/ # PDF reports
├── README.md # Project overview
└── requirements.txt # Dependencies


## 📊 What We've Done (Interim 1)

### ✅ Task 1: Data Analysis and Preprocessing

- Cleaned and merged datasets
- Handled missing values and duplicates
- Converted IP addresses to integers and mapped to country
- Extracted key time-based features:
  - `hour_of_day`
  - `day_of_week`
  - `time_since_signup`
- Explored class imbalance and proposed handling methods (e.g., SMOTE)

### 📌 Datasets Used
- `Fraud_Data.csv`  
- `IpAddress_to_Country.csv`  
- `creditcard.csv`  

## 📈 Upcoming (Interim 2 & Final)
- Train baseline and advanced models (Logistic Regression, Random Forest, XGBoost)
- Evaluate models using F1, AUC-PR
- Use SHAP for interpretability

## 🛠️ Setup Instructions


git clone https://github.com/kirubhel/fraud-detection-b5w8.git
cd fraud-detection-b5w8
pip install -r requirements.txt

📅 Timeline
Interim 1: Data preprocessing, EDA, and feature engineering

Interim 2: Model training & evaluation

Final: Model interpretation & report delivery

📬 Contact
Author: Kirubel Gizaw
Platform: Tenx (10 Academy Week 8)

---

### ✅ What I’ll Do Next:

1. Generate `requirements.txt`
2. Generate the Jupyter Notebook: `01_data_preprocessing_and_eda.ipynb`
3. Generate the `interim_1_report.pdf`

Do you want the GitHub `README.md` as a downloadable file, or should we start generating the notebook and PDF next?
