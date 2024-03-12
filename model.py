import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error

# Load the monthly message count data
data = pd.read_csv('monthly_message_count.csv')

# Convert 'month_start_date' column to datetime
data['month_start_date'] = pd.to_datetime(data['month_start_date'])

# Set 'month_start_date' as the index
data.set_index('month_start_date', inplace=True)

# Train-test split
train = data.iloc[:-1]
test = data.iloc[-1:]

# Fit SARIMAX model
order = (1, 1, 1)
seasonal_order = (1, 1, 1, 12)
model = SARIMAX(train['messages_count'], order=order, seasonal_order=seasonal_order)
result = model.fit()

# Generate predictions for the next month
forecast = result.get_forecast(steps=len(test))
forecast_values = forecast.predicted_mean

# Evaluate the model
mse = mean_squared_error(test['messages_count'], forecast_values)
rmse = np.sqrt(mse)

# Export the evaluation report as CSV
evaluation_report = pd.DataFrame({
    'RMSE': [rmse]
})
evaluation_report.to_csv('evaluation_report.csv', index=False)

# Combine actual and predicted values into a DataFrame
forecast_df = pd.DataFrame({
    'Date': test.index,
    'Actual': test['messages_count'].values,
    'Predicted': forecast_values.values
})

# Export the actual and predicted values as CSV
forecast_df.to_csv('forecast_values.csv', index=False)
