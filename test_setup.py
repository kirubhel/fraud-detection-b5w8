#!/usr/bin/env python3
"""
Test script to verify all required libraries are installed and working
"""

def test_imports():
    """Test all required imports"""
    try:
        # Standard libraries
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        import seaborn as sns
        
        # Machine Learning
        from sklearn.model_selection import train_test_split
        from sklearn.preprocessing import StandardScaler
        from sklearn.linear_model import LogisticRegression
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import classification_report, confusion_matrix
        
        # Imbalanced learning
        from imblearn.over_sampling import SMOTE
        from imblearn.under_sampling import RandomUnderSampler
        
        # SHAP
        import shap
        
        # XGBoost and LightGBM
        import xgboost as xgb
        import lightgbm as lgb
        
        # Plotly
        import plotly.express as px
        
        print("✅ All imports successful!")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_data_loading():
    """Test data loading"""
    try:
        import pandas as pd
        
        # Test loading data files
        fraud_data = pd.read_csv('data/Fraud_Data.csv')
        ip_country_data = pd.read_csv('data/IpAddress_to_Country.csv')
        credit_data = pd.read_csv('data/creditcard.csv')
        
        print(f"✅ Data loading successful!")
        print(f"   - Fraud Data: {fraud_data.shape}")
        print(f"   - IP Country Data: {ip_country_data.shape}")
        print(f"   - Credit Card Data: {credit_data.shape}")
        return True
        
    except Exception as e:
        print(f"❌ Data loading error: {e}")
        return False

def test_basic_modeling():
    """Test basic modeling functionality"""
    try:
        import pandas as pd
        import numpy as np
        from sklearn.model_selection import train_test_split
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import accuracy_score
        
        # Create dummy data
        X = np.random.randn(100, 5)
        y = np.random.randint(0, 2, 100)
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train model
        model = RandomForestClassifier(n_estimators=10, random_state=42)
        model.fit(X_train, y_train)
        
        # Make predictions
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        print(f"✅ Basic modeling test successful! Accuracy: {accuracy:.3f}")
        return True
        
    except Exception as e:
        print(f"❌ Modeling test error: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing setup...")
    print("=" * 50)
    
    tests = [
        ("Import Test", test_imports),
        ("Data Loading Test", test_data_loading),
        ("Basic Modeling Test", test_basic_modeling)
    ]
    
    all_passed = True
    for test_name, test_func in tests:
        print(f"\n🔍 Running {test_name}...")
        if not test_func():
            all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed! Ready to proceed with modeling.")
    else:
        print("⚠️  Some tests failed. Please check the errors above.") 