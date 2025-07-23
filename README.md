# Wallet Transaction Prediction API

This project is a FastAPI-based machine learning microservice that predicts outcomes based on wallet transaction features using a pre-trained linear regression model.

## 🧾 Project Structure

- `api_router.py`: FastAPI route for prediction.
- `linear_model.pkl`: Serialized linear regression model.
- `user-wallet-transactions.csv`: Sample dataset of wallet transactions.
- `Untitled.ipynb`: Jupyter notebook for data analysis and model training.
- `Transfer Dock_Text_20250723190831.txt`: Additional reference document.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- FastAPI
- Uvicorn
- NumPy
- Scikit-learn
- Pydantic

### Installation

```bash
pip install fastapi uvicorn numpy scikit-learn
```

### Running the API

```bash
uvicorn api_router:router --reload
```

### API Endpoint

#### POST `/predict`

**Request:**

```json
{
  "features": [0.2, 0.5, 0.3, ...]
}
```

**Response:**

```json
{
  "prediction": 123.45
}
```

## 📊 Model

The model used is a scikit-learn linear regression model trained on wallet transaction features. Refer to `Untitled.ipynb` for training details.

## 📁 Data

- `user-wallet-transactions.csv` contains anonymized wallet transaction records used for training/testing the model.

## 📝 License

MIT License
