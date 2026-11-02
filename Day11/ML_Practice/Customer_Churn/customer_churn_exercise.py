"""
Title: Supervised Classification Pipeline with Random Forest 
Description: A modular Python exercise script for loading clean customer churn data, 
             identifying target/predictors, encoding categorical variables, 
             scaling features, training a Random Forest classifier, evaluating performance, 
             and persisting the trained pipeline artifacts using joblib.
"""

# Step 0: Import necessary libraries
# TODO: Import pandas, numpy, train_test_split, StandardScaler, 
#       RandomForestClassifier, accuracy_score, classification_report, confusion_matrix, and joblib


def phase_1_discovery_and_target_identification():
    """
    [Phase 1] Discovery, Setup & Target/Predictor Identification
    - Goal: Load 'customer_churn_data.csv' and inspect structure.
    - Drop non-predictive identifiers (e.g., 'customer_id').
    - Identify Target feature (y: 'churn_flag') and Predictor features (X).
    """
    print("\n[PHASE 1] Discovery & Target Identification")
    print("-" * 65)
    # TODO: Load CSV file using pandas
    # TODO: Separate target feature y ('churn_flag') and predictor features X
    # TODO: Drop ID column ('customer_id')
    # TODO: Inspect class distribution of target variable
    pass


def phase_2_feature_engineering_and_encoding(X):
    """
    [Phase 2] Categorical Encoding & Feature Engineering
    - Goal: Encode categorical variables (e.g., 'contract_type', 'internet_service').
    - Optionally create engineered interaction features (e.g., charges per tenure month).
    """
    print("\n[PHASE 2] Feature Engineering & Categorical Encoding")
    print("-" * 65)
    # TODO: Apply one-hot encoding to categorical columns using pd.get_dummies()
    # TODO: Add engineered features if desired (e.g., X['avg_monthly_spend'] = X['total_charges'] / X['tenure_months'])
    # TODO: Display head of transformed feature matrix
    pass


def phase_3_scaling_and_train_test_split(X, y):
    """
    [Phase 3] Train-Test Split & Feature Scaling
    - Goal: Split dataset into Training and Testing sets.
    - Fit StandardScaler on training data and transform both train and test sets.
    """
    print("\n[PHASE 3] Data Splitting & Feature Scaling")
    print("-" * 65)
    # TODO: Perform train_test_split (test_size=0.2, random_state=42)
    # TODO: Initialize StandardScaler and scale numerical features
    # TODO: Fit scaler on X_train, transform X_train and X_test
    pass


def phase_4_model_training_and_testing(X_train_scaled, X_test_scaled, y_train, y_test):
    """
    [Phase 4] Random Forest Training & Classification Metrics
    - Goal: Train a RandomForestClassifier model.
    - Predict on test set and calculate evaluation metrics (Accuracy, Precision, Recall, F1).
    """
    print("\n[PHASE 4] Model Training & Test Set Evaluation")
    print("-" * 65)
    # TODO: Instantiate RandomForestClassifier(random_state=42) and fit on training data
    # TODO: Generate predictions on test set
    # TODO: Compute accuracy_score and classification_report
    pass


def phase_5_joblib_model_persistence(model, scaler, feature_names):
    """
    [Phase 5] Model Persistence & Future Deployment Setup
    - Goal: Save the trained model, fitted scaler, and feature list using joblib.
    - Test loading saved artifacts to run an inference on a new sample.
    """
    print("\n[PHASE 5] Model Persistence with Joblib")
    print("-" * 65)
    # TODO: Use joblib.dump() to save the model and scaler to disk (.joblib files)
    # TODO: Load saved artifacts using joblib.load() and perform sample inference
    pass


# ==========================================
# THE FACADE FUNCTION (Orchestrator)
# ==========================================

def run_ml_pipeline():
    """
    Facade function coordinating the entire classification pipeline.
    """
    print("=" * 65)
    print("STARTING SUPERVISED CLASSIFICATION LIFECYCLE (Random Forest)")
    print("=" * 65)
    
    # Executing phases chronologically
    # X, y = phase_1_discovery_and_target_identification()
    # X_encoded = phase_2_feature_engineering_and_encoding(X)
    # X_tr_scaled, X_te_scaled, y_tr, y_te, scaler = phase_3_scaling_and_train_test_split(X_encoded, y)
    # model = phase_4_model_training_and_testing(X_tr_scaled, X_te_scaled, y_tr, y_te)
    # phase_5_joblib_model_persistence(model, scaler, X_encoded.columns.tolist())


# ==========================================
# MAIN GUARD
# ==========================================
if __name__ == "__main__":
    run_ml_pipeline()