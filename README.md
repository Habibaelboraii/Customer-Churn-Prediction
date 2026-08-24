# 📊 Customer Churn Prediction

## 📌 Project Overview

This project aims to predict whether a customer is likely to churn from a telecommunications company using Machine Learning.

The project covers the complete Machine Learning workflow, including:

* Data Understanding
* Exploratory Data Analysis (EDA)
* Data Cleaning
* Data Preprocessing
* Feature Encoding
* Feature Scaling
* Model Training
* Hyperparameter Tuning
* Model Evaluation
* Streamlit Deployment

The final trained model is integrated into a **Streamlit web application** that allows users to enter customer information and receive a churn prediction.

---

## 🎯 Project Objective

Customer churn is an important business problem because losing customers can negatively affect a company's revenue.

The main objective of this project is to build a Machine Learning classification model that predicts whether a customer will:

* 🔴 **Churn**
* 🟢 **Not Churn**

This can help companies identify customers who are more likely to leave and take appropriate customer retention actions.

---

## 📊 Dataset

The project uses the **Telco Customer Churn Dataset**.

The dataset contains customer demographic information, services, contract details, and billing information.

### 🔍 Features Description

| Feature              | Description                                                      |
| -------------------- | ---------------------------------------------------------------- |
| **gender**           | Customer's gender                                                |
| **SeniorCitizen**    | Indicates whether the customer is a senior citizen               |
| **Partner**          | Indicates whether the customer has a partner                     |
| **Dependents**       | Indicates whether the customer has dependents                    |
| **tenure**           | Number of months the customer has stayed with the company        |
| **PhoneService**     | Indicates whether the customer has phone service                 |
| **MultipleLines**    | Indicates whether the customer has multiple phone lines          |
| **InternetService**  | Type of internet service used by the customer                    |
| **OnlineSecurity**   | Indicates whether the customer has online security service       |
| **OnlineBackup**     | Indicates whether the customer has online backup service         |
| **DeviceProtection** | Indicates whether the customer has device protection service     |
| **TechSupport**      | Indicates whether the customer has technical support service     |
| **StreamingTV**      | Indicates whether the customer has a TV streaming service        |
| **StreamingMovies**  | Indicates whether the customer has a movie streaming service     |
| **Contract**         | Type of contract: Month-to-month, One year, or Two year          |
| **PaperlessBilling** | Indicates whether the customer uses paperless billing            |
| **PaymentMethod**    | Payment method used by the customer                              |
| **MonthlyCharges**   | Amount charged to the customer per month                         |
| **TotalCharges**     | Total amount charged to the customer                             |
| **Churn**            | Target variable indicating whether the customer left the company |

### 🎯 Target Variable

The target variable is **Churn**:

* `Yes` → The customer churned.
* `No` → The customer stayed with the company.

---

## 🔎 Exploratory Data Analysis

Several visualizations were created to understand the dataset and investigate the relationship between customer characteristics and churn.

The analysis includes:

* Churn distribution
* Contract type vs. churn
* Payment method vs. churn
* Internet service vs. churn
* Phone service vs. churn
* Tenure vs. churn
* Monthly charges vs. churn
* Total charges vs. churn
* Other relevant feature comparisons

These visualizations helped identify patterns and relationships between customer characteristics and churn.

---

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

1. Checked the dataset structure and data types.
2. Checked for missing values.
3. Handled missing values where necessary.
4. Checked for duplicate records.
5. Explored numerical and categorical features.
6. Encoded categorical features into numerical values.
7. Applied feature scaling where required.
8. Split the dataset into training and testing sets.

The preprocessing objects were saved and reused in the Streamlit application to ensure that new customer data is processed consistently with the training data.

---

## 🤖 Machine Learning Models

Several classification models were explored and evaluated, including:

* **Logistic Regression**
* **Support Vector Machine (SVM)**
* **ٌRandom Forest**
* **ٌDecision Tree**
* **XGBoost**

The models were compared using multiple evaluation metrics to select the most suitable model for the churn prediction task.

---

## ⚙️ Hyperparameter Tuning

Hyperparameter tuning was performed to improve the performance of the machine learning models.

Different hyperparameter combinations were evaluated, and the best-performing configuration was selected for the final model.

---

## 📈 Model Evaluation

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

### 🏆 Final Model

The final model used in the deployed application is:

**XGBoost Classifier**

XGBoost was selected based on its overall performance on the evaluation metrics.

### 📊 Final Model Performance

| Metric    |        Score |
| --------- | -----------: |
| Accuracy  | `0,78` |
| Precision | `0.548077` |
| Recall    | `0.655172` |
| F1-Score  | `0.596859` |

> Replace `YOUR_SCORE` with the actual results of your final XGBoost model.

---

## ⭐ Why XGBoost?

XGBoost was selected as the final model because it provided strong classification performance for the customer churn prediction problem.

It can capture nonlinear relationships between customer features and the target variable and works effectively with structured/tabular data.

---

## 🌐 Streamlit Application

A Streamlit web application was developed to make the trained model easy to use.

The application allows users to enter customer information and receive a churn prediction.

### 🔄 Application Workflow

```text
Customer Information
        ↓
Data Preprocessing
        ↓
Encoding
        ↓
Scaling
        ↓
XGBoost Model
        ↓
Churn Prediction
```

### 🎯 Prediction Output

The application predicts whether the customer is likely to:

🟢 **Not Churn**

or

🔴 **Churn**

The application uses the saved:

* XGBoost model
* Encoder
* Scaler

to process the input data and generate the prediction.

### 🚀 Live Demo

**Streamlit App:**

``

---

## 🗂️ Project Structure

```text
customer-churn-prediction/
│
├── app.py
├── xgb_model.pkl
├── scaler.pkl
├── encoder.pkl
├── requirements.txt
├── README.md
├── .gitignore
│
└── images/
    └── streamlit_app.png
```

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **XGBoost**
* **Matplotlib**
* **Seaborn**
* **Streamlit**
* **Git & GitHub**

---

## 📦 Installation

### 1. Clone the Repository

```bash

```

### 2. Navigate to the Project Directory

```bash
cd customer-churn-prediction
```

### 3. Install the Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Understanding
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Engineering
   ↓
Categorical Encoding
   ↓
Feature Scaling
   ↓
Train/Test Split
   ↓
Model Training
   ↓
Hyperparameter Tuning
   ↓
Model Evaluation
   ↓
XGBoost Final Model
   ↓
Streamlit Application
   ↓
Customer Churn Prediction
```

---

## 🏫 Epsilon AI

This project was developed as part of my training at **Epsilon AI Academy Egypt**.

### Main Epsilon AI Repository

`PASTE THE OFFICIAL EPSILON AI MAIN REPOSITORY LINK HERE`

> The official Epsilon AI repository should be linked here according to the project submission requirements.

---

## 🚀 Future Improvements

Possible future improvements include:

* Improving model performance through additional feature engineering.
* Trying additional ensemble models.
* Adding customer churn probability.
* Improving the Streamlit user interface.
* Adding model explainability using SHAP.
* Deploying the application publicly.

---

## 👩‍💻 Author

**Habiba Saber**

Machine Learning / Data Science Enthusiast

