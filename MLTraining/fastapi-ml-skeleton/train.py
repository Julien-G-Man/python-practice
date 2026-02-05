import os
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Get the path of the current folder (src)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define paths relative to 'src'
DATA_PATH = os.path.join(BASE_DIR, '..', 'data', 'data.csv')
MODEL_SAVE_PATH = os.path.join(BASE_DIR, '..', 'models', 'my_model.joblib')

# Load data
df = pd.read_csv(DATA_PATH)
X = df[['feature1', 'feature2']]
y = df['target']

# Train
model = RandomForestRegressor()
model.fit(X, y)

# Save
joblib.dump(model, MODEL_SAVE_PATH)
print(f"Model saved to: {MODEL_SAVE_PATH}")