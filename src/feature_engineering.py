from sklearn.preprocessing import StandardScaler
import pandas as pd

def process_features(df):
    X = df.drop('Yield', axis=1)
    y = df['Yield']

    X = pd.get_dummies(X)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, scaler, X.columns