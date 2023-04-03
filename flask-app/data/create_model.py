# Import the necessary libraries
import pandas as pd
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load the data from the CSV file into a pandas DataFrame
def read_df():

    """return a renamed dataframe"""

    data_path='flask-app\data\data_set_prepared.csv'
    df = pd.read_csv(data_path)
    df.rename(columns={
    'Potential_temperature_C':'Temperture',
    'Practical_salinity':'Salinity',
    'Potential_density_anomaly_kgm3':'Density',
    'Pressure_decibar':'Pressure',
    'Serial_date_number_base_date_1_January_0000':'Date',
    'Bottom_Depth_m':'Bottom Depth'
    },inplace=True)
    df['Date'] = [datetime.fromordinal(int(date)) for date in df['Date']]
    return df

data=read_df()

# Extract the input features (temperature and salinity) and the target variable (date)
X = data[['Temperture', 'Salinity']]
y = data['Date']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and fit the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make a prediction using the model on the test set
prediction = model.predict(X_test)

# Evaluate the accuracy of the model using the R-squared score
r_squared = model.score(X_test, y_test)
print('R-squared:', r_squared)