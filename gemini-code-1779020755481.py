import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print('Modules installed successfully!!!...')

# Path ko sahi kiya
path = 'customer_data.csv'  
df = pd.read_csv(path)

# Print laga diya
print("--- Data Head ---")
print(df.head()) 

X = df[['total_purchases']]
y = df['total_spent']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training data shape: {X_train.shape}, {y_train.shape}")
print(f"Testing data shape: {X_test.shape}, {y_test.shape}")

lr = LinearRegression()
lr.fit(X_train, y_train)

print(f"Intercept: {lr.intercept_}")
print(f"Coefficient: {lr.coef_}")

y_pred = lr.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"\nMean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R-squared Score: {r2:.2f}")

# Naye data par Sahi tarike se prediction
new_customer = pd.DataFrame({'total_purchases': [15]})
pred = lr.predict(new_customer)
print(f'\nEstimated spending for 15 purchases: ${pred[0]:.2f}')