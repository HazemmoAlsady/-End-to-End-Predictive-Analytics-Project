"""Model configuration and constants"""

# Feature configuration
REQUIRED_FEATURES = ['Product_Category', 'Price', 'Discount', 'Customer_Segment', 'Marketing_Spend']

FEATURE_TYPES = {
    'Product_Category': 'categorical',
    'Price': 'numerical',
    'Discount': 'numerical',
    'Customer_Segment': 'categorical',
    'Marketing_Spend': 'numerical'
}

# Validation rules
VALIDATION_RULES = {
    'Price': {'min': 0, 'max': None},
    'Discount': {'min': 0, 'max': 100},
    'Marketing_Spend': {'min': 0, 'max': None}
}

# Model hyperparameters
MODEL_PARAMS = {
    'test_size': 0.2,
    'random_state': 42
}
