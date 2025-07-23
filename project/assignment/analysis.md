# Analysis Report: Wallet Transaction Prediction

## 📂 Dataset Overview

The dataset `user-wallet-transactions.csv` includes multiple wallet transaction records. Each row represents a transaction with multiple numerical features.

### Sample Columns (inferred):

- Transaction amount
- Time or timestamp
- Type (credit/debit)
- Account balance after transaction
- Sender/receiver info (possibly encoded)

## ⚙️ Model Description

A `LinearRegression` model from scikit-learn was used. It was trained to predict a target variable (e.g., transaction risk, amount, or balance) based on input features from the dataset.

### Model Training Highlights:

- Input features normalized using NumPy.
- Training process conducted in `Untitled.ipynb`.
- Model serialized using `pickle`.

## 🔍 API Functionality

The FastAPI router exposes a POST endpoint `/predict` that accepts a list of numerical features. It reshapes the input, performs prediction, and returns a floating-point result.

### Error Handling:

- Any invalid input raises a 400 error with a descriptive message.

## 🧪 Sample Input & Output

**Input JSON:**

```json
{
  "features": [1500.75, 2, 0, 45000.0]
}
```

**Predicted Output:**

```json
{
  "prediction": 47250.86
}
```

## 🔒 Notes

- Ensure `linear_model.pkl` is in the same directory as `api_router.py`.
- Only numerical features supported.
- No authentication or rate-limiting included — use in secured environments.
