import os

print("🌾 Crop Yield Prediction System")

print("\n1. Convert Dataset")
print("2. Train Model")
print("3. Generate Graphs")
print("4. Run Web App")

choice = input("Enter your choice: ")

if choice == "1":
    os.system("python convert_data.py")

elif choice == "2":
    os.system("python src/train_full_model.py")

elif choice == "3":
    os.system("python src/visualize.py")

elif choice == "4":
    os.system("streamlit run app/app.py")

else:
    print("Invalid choice!")