import pandas as pd

def load_data():
    df = pd.read_csv("data/crop_data.csv")
    df = df.dropna()
    return df