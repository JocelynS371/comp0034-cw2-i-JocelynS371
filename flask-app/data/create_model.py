# Import the necessary libraries
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error

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
    #df['Date'] = [datetime.fromordinal(int(date)) for date in df['Date']]
    return df

data=read_df()

# extract the features and target variable
X = data[['Date', 'Longitude', 'Latitude']]
y = data['Temperture']

# split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# for loop to optimise model
n=np.arange(0,501,100)
for n_estimators in n:
    # create the SGD regression model with default settings
    model = GradientBoostingRegressor(n_estimators=n_estimators,learning_rate=0.6,max_depth=4,random_state=0)

    # fit the model with training data
    model.fit(X_train, y_train)

    # make predictions with test data
    y_pred = model.predict(X_test)

    # calculate the R-squared score
    print('n_estimator:',n_estimators)
    r_squared = r2_score(y_test, y_pred)
    print('R-squared score:', r_squared)
    error=mean_absolute_error(y_test,y_pred)
    print('mean absolute error:',error)
