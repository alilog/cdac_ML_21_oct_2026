"""
Title: End-to-End Supervised Machine Learning Pipeline (Student Exercise)
Description: A modular Python exercise script for loading clean housing data, 
             identifying target/predictors, encoding categorical variables, 
             scaling features, training a regression model, evaluating performance, 
             and persisting the trained pipeline artifacts using joblib.

"""

# Step 0: Import necessary libraries
# TODO: Import pandas, numpy, train_test_split, StandardScaler, OneHotEncoder / ColumnTransformer,
#       LinearRegression (or RandomForestRegressor), mean_squared_error, mean_absolute_error, r2_score, and joblib


def phase_1_discovery_and_target_identification():
    """
    [Phase 1] Discovery, Setup & Target/Predictor Identification 
    - Goal: Load 'housing_ml_data.csv' and inspect structure.
    - Drop non-predictive identifiers (e.g., 'house_id').
    - Identify Target feature (y) and Predictor features (X).
    """
    print("\n[PHASE 1] Discovery & Target Identification ")
    print("-" * 65)
    # TODO: Load CSV file using pandas
    # TODO: Separate target feature y ('price_usd') and predictor features X
    # TODO: Drop ID column ('house_id')
    # TODO: Print shapes of X and y
    pass


def phase_2_feature_engineering_and_encoding(X):
    """
    [Phase 2] Categorical Encoding & Feature Engineering (10 Marks)
    - Goal: Encode categorical variables (e.g., 'location_type', 'has_garage').
    - Optionally create engineered interaction features (e.g., sqft per bedroom).
    """
    print("\n[PHASE 2] Feature Engineering & Categorical Encoding ")
    print("-" * 65)
    # TODO: Apply one-hot encoding or ordinal encoding to categorical columns
    # TODO: Add engineered features if needed (e.g., X['sqft_per_room'] = X['square_feet'] / X['num_bedrooms'])
    # TODO: Display head of transformed feature matrix
    pass


def phase_3_scaling_and_train_test_split(X, y):
    """
    [Phase 3] Train-Test Split & Feature Scaling (10 Marks)
    - Goal: Split dataset into 80% Training and 20% Testing sets.
    - Fit StandardScaler on training data and transform both train and test sets.
    """
    print("\n[PHASE 3] Data Splitting & Feature Scaling ")
    print("-" * 65)
    # TODO: Perform train_test_split (test_size=0.2, random_state=42)
    # TODO: Initialize StandardScaler and scale numerical features
    # TODO: Fit scaler on X_train, transform X_train and X_test
    pass


def phase_4_model_training_and_testing(X_train_scaled, X_test_scaled, y_train, y_test):
    """
    [Phase 4] Model Training & Testing Metrics (10 Marks)
    - Goal: Train a regression algorithm (e.g., LinearRegression / RandomForest).
    - Predict on test set and calculate evaluation metrics (MAE, RMSE, R-squared).
    """
    print("\n[PHASE 4] Model Training & Test Set Evaluation ")
    print("-" * 65)
    # TODO: Instantiate regression model and fit on (X_train_scaled, y_train)
    # TODO: Generate predictions on X_test_scaled
    # TODO: Compute MAE, RMSE, and R2_score
    pass


def phase_5_joblib_model_persistence(model, scaler, feature_names):
    """
    [Phase 5] Model Persistence & Future Deployment Setup (5 Marks)
    - Goal: Save the trained model, fitted scaler, and feature list using joblib.
    - Test loading saved artifacts to run an inference on a new sample.
    """
    print("\n[PHASE 5] Model Persistence with Joblib ")
    print("-" * 65)
    # TODO: Use joblib.dump() to save the model and scaler to disk (.joblib files)
    # TODO: Load saved artifacts using joblib.load() and perform sample inference
    pass


# ==========================================
# THE FACADE FUNCTION (Orchestrator)
# ==========================================

def run_ml_pipeline():
    """
    Facade function coordinating the entire machine learning pipeline.
    """
    print("=" * 65)
    print("STARTING END-TO-END MACHINE LEARNING LIFECYCLE ")
    print("=" * 65)
    
    # Executing phases chronologically
    # X, y = phase_1_discovery_and_target_identification()
    # X_encoded = phase_2_feature_engineering_and_encoding(X)
    # X_tr_scaled, X_te_scaled, y_tr, y_te, scaler = phase_3_scaling_and_train_test_split(X_encoded, y)
    # model, metrics = phase_4_model_training_and_testing(X_tr_scaled, X_te_scaled, y_tr, y_te)
    # phase_5_joblib_model_persistence(model, scaler, X_encoded.columns.tolist())


# ==========================================
# MAIN GUARD
# ==========================================
if __name__ == "__main__":
    run_ml_pipeline()