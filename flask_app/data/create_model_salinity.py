# Import the necessary libraries
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_absolute_error
from sklearn.ensemble import GradientBoostingRegressor

# Load the data from the CSV file into a pandas DataFrame
def read_df(): 

    """return a renamed dataframe"""

    data_path = 'flask-app\data\data_set_prepared.csv'
    df = pd.read_csv(data_path)
    df.rename(columns = {
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
y = data['Salinity']

# split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# trial and error, n_estimator=440, learning rate=0.5
# for loop to optimise model
#n=np.arange(0,1.1,0.1)
#r_squared=[]
#abs_error=[]
#for learning_rate in n:
    # create the SGD regression model with default settings
model = GradientBoostingRegressor(n_estimators=440,learning_rate=0.5,max_depth=4,random_state=0)

# fit the model with training data
model.fit(X_train, y_train)

# make predictions with test data
y_pred = model.predict(X_test)

# calculate the R-squared score

r_squared=r2_score(y_test, y_pred)
abs_error=mean_absolute_error(y_test,y_pred)
print('r square:',r_squared)
print('mean_absolute_error:',abs_error)
filename = 'model_temp.sav'
pickle.dump(model, open(filename, 'wb'))
#plt.figure(1)
#r_plot=plt.plot(n,r_squared)
#plt.title('r_square_values')
#plt.figure(2)
#e_plot=plt.plot(n,abs_error)
#plt.title('error_values')
#plt.show()