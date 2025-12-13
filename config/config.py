"""Project Configuration"""
import os

class Config:
    """Base configuration"""
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    API_HOST = os.getenv('API_HOST', '0.0.0.0')
    API_PORT = int(os.getenv('API_PORT', 5000))
    DEBUG = os.getenv('FLASK_DEBUG', False)
    
    # Model paths
    MODEL_DIR = 'models'
    MODEL_PATH = os.path.join(MODEL_DIR, 'revenue_model.pkl')
    LE_PRODUCT_PATH = os.path.join(MODEL_DIR, 'le_product.pkl')
    LE_SEGMENT_PATH = os.path.join(MODEL_DIR, 'le_segment.pkl')
    
    # Data paths
    DATA_DIR = 'data'
    RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw')
    PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')
    
    # Logging
    LOG_DIR = 'logs'
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.path.join(LOG_DIR, 'api.log')

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
