"""Model Training Script - Using Random Forest (from Airbnb_Project.ipynb)"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def train_model():
    """Train units prediction model using Random Forest"""
    
    logger.info("="*50)
    logger.info("="*50)
    logger.info("Starting Model Training (Linear Regression - Revenue Target)")
    logger.info("="*50)
    logger.info("="*50)
    
    # Load dataset
    logger.info("Loading dataset...")
    data_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'Ecommerce_Sales_Prediction_Dataset.csv')
    df = pd.read_csv(data_path)
    logger.info(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    
    # Preprocessing - Extract date features
    logger.info("Preprocessing data...")
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    df['Day'] = df['Date'].dt.day
    df['Month'] = df['Date'].dt.month
    df.drop('Date', axis=1, inplace=True)
    
    # Encode categorical features
    le_product = LabelEncoder()
    df['Product_Category'] = le_product.fit_transform(df['Product_Category'])
    
    le_segment = LabelEncoder()
    df['Customer_Segment'] = le_segment.fit_transform(df['Customer_Segment'])
    
    logger.info(f"Product categories: {list(le_product.classes_)}")
    logger.info(f"Customer segments: {list(le_segment.classes_)}")
    
    # Feature Engineering - Create Effective Price
    df['Effective_Price'] = df['Price'] * (1 - df['Discount'] / 100)
    
    # Calculate Revenue (Target)
    df['Revenue'] = df['Effective_Price'] * df['Units_Sold']
    
    # Features & Target
    X = df[['Effective_Price', 'Discount', 'Marketing_Spend', 'Day', 'Month']]
    y = df['Revenue']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    logger.info(f"Train set: {X_train.shape[0]} | Test set: {X_test.shape[0]}")
    
    # Train model - Linear Regression (Requested by user)
    logger.info("Training Linear Regression model...")
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    
    logger.info(f"MAE: {mae:.4f}")
    logger.info(f"RMSE: {rmse:.4f}")
    logger.info(f"R² Score: {r2:.4f}")
    
    # Save artifacts
    logger.info("Saving model artifacts...")
    model_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'models')
    os.makedirs(model_dir, exist_ok=True)
    
    joblib.dump(model, os.path.join(model_dir, 'revenue_model.pkl'))
    joblib.dump(le_product, os.path.join(model_dir, 'le_product.pkl'))
    joblib.dump(le_segment, os.path.join(model_dir, 'le_segment.pkl'))
    
    logger.info("✓ Model training complete!")
    logger.info("="*50)
    
    return model, le_product, le_segment

if __name__ == '__main__':
    train_model()
