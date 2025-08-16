# **GDP Prediction Project Report**

## **1. Title of the Project**

GDP Prediction Using Machine Learning

## **2. Abstract**

This project aims to predict a country's Gross Domestic Product (GDP) using various socio-economic indicators. By leveraging machine learning models, particularly Random Forest and Decision Tree Regressors, we analyze historical GDP data to identify key influencing factors. The study focuses on optimizing model accuracy while providing meaningful insights into economic trends.

## **3. Introduction**

GDP is a crucial measure of a nation's economic health. Understanding its contributing factors helps policymakers and businesses make informed decisions. This study applies machine learning techniques to predict GDP based on multiple features, such as literacy rates, industry contributions, and mobile phone penetration.

## **4. Objective of the Study**

- To develop an accurate predictive model for GDP.
- To identify key socio-economic indicators influencing GDP.
- To compare different machine learning models for optimal performance.
- To provide insights into economic trends based on feature importance.

## **5. Literature Review / Background Study**

Several studies have used traditional econometric models for GDP prediction. Recent advancements in machine learning have enabled more accurate and scalable GDP forecasting. This project builds upon past research, incorporating data preprocessing, feature selection, and model tuning to improve prediction accuracy.

## **6. Research Methodology**

### **6.1 Data Collection**

- Dataset Source: Public economic databases, trade journals, and statistical reports.
- Data Preprocessing: Handling missing values, standardizing formats, and feature engineering.

### **6.2 Machine Learning Models Used**

- **Linear Regression**: Baseline model for GDP prediction.
- **Random Forest Regressor**: Applied hyperparameter tuning for optimal performance.
- **Decision Tree Regressor**: Compared performance against Random Forest.

### **6.3 Model Training & Evaluation**

- Splitting dataset into training and testing sets (80-20 split).
- Evaluating models using Mean Squared Error (MSE) and R-squared (R²) score.
- Feature importance analysis to interpret model decisions.

## **7. Data Analysis & Interpretation**

- Key features affecting GDP:
  - **Phones per 1000 people** (Highest Importance: 81.3%)
  - **Literacy Rate** (7.5%)
  - **Industry Contribution** (3.1%)
- Model Performance:
  - **Random Forest (Best Model)**: MSE: 13,066,490.93, R²: 0.88
  - **Decision Tree**: MSE: Higher than RF, Lower R²

## **8. Results & Discussion**

- Random Forest outperformed other models in predictive accuracy.
- The number of mobile phones per 1000 people showed the highest correlation with GDP.
- Feature selection and hyperparameter tuning significantly improved model performance.

## **9. Recommendations & Conclusion**

- **Policy Implications**: Governments should enhance digital infrastructure and literacy programs.
- **Future Scope**: Incorporating real-time economic indicators for more dynamic predictions.
- The study demonstrated that machine learning models, particularly Random Forest, can effectively predict GDP with high accuracy.

## **10. Bibliography & References**

- Official World Bank GDP datasets
- Machine Learning research papers on economic forecasting
- Articles on feature importance in regression models
- APA format citations for all referenced sources

