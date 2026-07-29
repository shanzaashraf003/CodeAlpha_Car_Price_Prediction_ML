import joblib
import pandas as pd

# Load model
model = joblib.load("../models/car_price_model.pkl")

# Example input
sample = pd.DataFrame({
    "Present_Price": [5.59],
    "Driven_kms": [27000],
    "Owner": [0],
    "Car_Age": [11],
    "Fuel_Type_Diesel": [0],
    "Fuel_Type_Petrol": [1],
    "Selling_type_Individual": [0],
    "Transmission_Manual": [1]
})

prediction = model.predict(sample)

print(f"Predicted Car Price: {prediction[0]:.2f} Lakhs")