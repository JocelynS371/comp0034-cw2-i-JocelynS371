import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.ensemble import GradientBoostingRegressor


plot = False
optimise = False


def read_df():
    """Return a renamed dataframe."""
    data_path = 'flask_app/data/data_set_prepared.csv'
    df = pd.read_csv(data_path)
    df.rename(columns={
        'Potential_temperature_C': 'Temperature',
        'Practical_salinity': 'Salinity',
        'Potential_density_anomaly_kgm3': 'Density',
        'Pressure_decibar': 'Pressure',
        'Serial_date_number_base_date_1_January_0000': 'Date',
        'Bottom_Depth_m': 'Bottom Depth'
    }, inplace=True)
    return df


data = read_df()
X = data[['Date', 'Longitude', 'Latitude']]
y = data['Temperature']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

if optimise:
    n = np.arange(0.3, 0.4, 0.01)
    r_squared = []
    abs_error = []
    for opt in n:
        model = GradientBoostingRegressor(n_estimators=240, learning_rate=opt, max_depth=4, random_state=0)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        print(f'progress:{opt}')
        if plot:
            r_squared.append(r2_score(y_test, y_pred))
            abs_error.append(mean_absolute_error(y_test, y_pred))
        else:
            print(r2_score(y_test, y_pred))
            print(mean_absolute_error(y_test, y_pred))
    if plot:
        plt.figure(1)
        r_plot = plt.plot(n, r_squared)
        plt.title('r_square_values')
        plt.figure(2)
        e_plot = plt.plot(n, abs_error)
        plt.title('error_values')
        plt.show()
else:
    model = GradientBoostingRegressor(n_estimators=240, learning_rate=0.34, max_depth=4, random_state=0)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(r2_score(y_test, y_pred))
    print(mean_absolute_error(y_test, y_pred))
    filename = 'model_temp.sav'
    pickle.dump(model, open(filename, 'wb'))
