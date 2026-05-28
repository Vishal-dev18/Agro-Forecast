import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor, VotingRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score, mean_squared_error

# -------------------------------
# LOAD & CLEAN DATA
# -------------------------------
df = pd.read_csv("data/crop_data.csv")

# Convert Yield to numeric (fix hidden errors)
df['Yield'] = pd.to_numeric(df['Yield'], errors='coerce')

# Remove missing values
df = df.dropna()

print("Dataset shape after cleaning:", df.shape)

# -------------------------------
# FEATURES & TARGET
# -------------------------------
X = df[['Crop', 'Season', 'State', 'Area', 'Annual_Rainfall', 'Fertilizer']]
y = df['Yield']

# One-hot encoding
X = pd.get_dummies(X)

# Save column structure
pickle.dump(X.columns, open("models/columns.pkl", "wb"))

# -------------------------------
# TRAIN-TEST SPLIT
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# SCALING
# -------------------------------
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Save scaler
pickle.dump(scaler, open("models/scaler.pkl", "wb"))

# -------------------------------
# INDIVIDUAL MODELS
# -------------------------------
rf = RandomForestRegressor(n_estimators=100, random_state=42)
svr = SVR()
knn = KNeighborsRegressor()

print("Training individual models...")

rf.fit(X_train, y_train)
svr.fit(X_train, y_train)
knn.fit(X_train, y_train)

# -------------------------------
# ENSEMBLE MODEL
# -------------------------------
ensemble = VotingRegressor([
    ('rf', rf),
    ('svr', svr),
    ('knn', knn)
])

print("Training ensemble model...")

ensemble.fit(X_train, y_train)

# -------------------------------
# EVALUATION
# -------------------------------
y_pred = ensemble.predict(X_test)

r2 = r2_score(y_test, y_pred)

# Fix for old sklearn version
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("\n📊 MODEL PERFORMANCE")
print("R2 Score:", round(r2, 3))
print("RMSE:", round(rmse, 3))

# -------------------------------
# SAVE MODEL
# -------------------------------
pickle.dump(ensemble, open("models/model.pkl", "wb"))

print("\n✅ Ensemble Model Trained & Saved Successfully!")