# 📊 E-Commerce Revenue Prediction
**Forecast & Predictive Analytics Project**

---

## 📌 Project Description
This project focuses on predicting **e-commerce revenue** using historical sales data.
It demonstrates a complete end-to-end predictive analytics workflow including
data preprocessing, exploratory data analysis, model building, and evaluation.

---

## 🎯 Problem Statement
Accurate revenue prediction is essential for e-commerce businesses to:
- Plan marketing budgets
- Forecast future sales
- Improve pricing and promotion strategies

The goal of this project is to predict **Revenue** based on pricing, discounts,
customer segments, and marketing spend.

---

## 📂 Dataset Information
**Dataset Name:** E-commerce Sales Prediction Dataset

**Main Features:**
- Product_Category  
- Price  
- Discount  
- Customer_Segment  
- Marketing_Spend  
- Date  

**Target Variable:**
- **Revenue** (calculated from Effective Price × Units Sold)

---

## 🔧 Data Preprocessing
The following preprocessing steps were applied:
- Converted date into numerical features (Day, Month)
- Encoded categorical variables using Label Encoding
- Created new features:
  - Effective_Price
  - Revenue
- Selected the most relevant features for modeling

---

## 📈 Exploratory Data Analysis (EDA)
EDA was performed to analyze:
- The relationship between marketing spend and revenue
- The impact of pricing and discounts on sales

Visualizations were used to identify trends and patterns in the data.

---

## 🤖 Machine Learning Models
The following regression models were implemented and compared:
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

---

## 🧪 Model Evaluation
Models were evaluated using:
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

### ✅ Best Model
**Linear Regression** achieved the best performance with an R² score of approximately **82%**,
indicating strong predictive capability.

---

## 📊 Results & Visualization
A comparison between actual and predicted revenue values shows that the model
successfully captures the overall sales trend.

---

## 🏁 Conclusion
This project demonstrates a complete **end-to-end predictive analytics workflow**.
The results show that pricing, discounts, and marketing spend play a significant role
in determining e-commerce revenue.

---

## 🛠️ Technologies Used
- Python
- Pandas & NumPy
- Scikit-learn
- Matplotlib & Seaborn
- Google Colab

---

## ▶️ How to Run
1. Upload the dataset to Google Colab
2. Run the notebook cells step by step
3. Review model evaluation metrics and predictions

---

## 👨‍🎓 Author
This project was developed as part of the **Forecast & Predictive Analytics** course.
