from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine
# read csv into panda dataframe
def read_df():

    """return a renamed dataframe"""

    data_path=Path(__file__).parent.joinpath('data_set_prepared.csv')
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

db_file = Path(__file__).parent.joinpath("data.db")
engine = create_engine("sqlite:///" + str(db_file), echo=False)
# Write the data to a table in the sqlite database 
data.to_sql("data", engine, if_exists="append")