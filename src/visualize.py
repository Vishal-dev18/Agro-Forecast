import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
df = pd.read_csv("data/crop_data.csv")

# Create folder if not exists
os.makedirs("outputs/graphs", exist_ok=True)

# 1. Crop-wise Yield
plt.figure()
df.groupby('Crop')['Yield'].mean().plot(kind='bar')
plt.title("Average Yield per Crop")
plt.xlabel("Crop")
plt.ylabel("Yield")
plt.savefig("outputs/graphs/crop_yield.png")
plt.close()

# 2. Area vs Yield
plt.figure()
plt.scatter(df['Area'], df['Yield'])
plt.xlabel("Area")
plt.ylabel("Yield")
plt.title("Area vs Yield")
plt.savefig("outputs/graphs/area_vs_yield.png")
plt.close()

# 3. Season-wise Yield
plt.figure()
df.groupby('Season')['Yield'].mean().plot(kind='bar')
plt.title("Yield by Season")
plt.savefig("outputs/graphs/season_yield.png")
plt.close()

print("✅ Graphs saved in outputs/graphs/")