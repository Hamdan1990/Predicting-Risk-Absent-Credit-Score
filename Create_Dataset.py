import pandas as pd
import numpy as np
import requests
from datetime import datetime, timedelta
from fredapi import Fred

fred = Fred(api_key=‘0159307479eeef14ee8068e06e4085aa’)

loans_df = pd.read_table(‘loans.tsv’, sep=‘\t’)
loans_df[‘issue_d’] = pd.to_datetime(loans_df[‘issue_d’].apply(lambda x: x.zfill(6)), format=‘%y-%b’)
loans_df.set_index([‘issue_d’], inplace=True)
loans_df = loans_df.to_period(‘M’).to_timestamp(‘M’)

r = requests.get(‘https://www.zillow.com/ajax/homevalues/data/timeseries.json?r=102001&m=zhvi_plus_forecast&dt=1')
home_index_history_json = r.json()[‘102001;zhvi_plus_forecast;1’][‘data’]
home_index = {‘dates’: [], ‘z_index’: []}
for a in home_index_history_json:
    home_index[‘dates’].append(datetime(1970, 1, 1) + timedelta(milliseconds=a[‘x’]))
    home_index[‘z_index’].append(a[‘y’])

zillow_df = pd.DataFrame(home_index, columns=[‘dates’, ‘z_index’])
zillow_df.set_index([‘dates’], inplace=True)
zillow_df= zillow_df.to_period(‘M’).to_timestamp(‘M’)

usa_cpi = fred.get_series_latest_release(‘CPIAUCSL’).to_frame()
usa_cpi.columns = [‘cpi’]
usa_cpi.index = usa_cpi.index.to_period(‘M’).to_timestamp(‘M’)

usa_treasury = fred.get_series_latest_release(‘TB3MS’).to_frame()
usa_treasury.columns = [‘3_month_treasury’]
usa_treasury.index = usa_treasury.index.to_period(‘M’).to_timestamp(‘M’)

loans_df = loans_df.join(zillow_df)
loans_df = loans_df.join(usa_cpi)
loans_df = loans_df.join(usa_treasury)

loans_df.to_csv(‘cleaned_loans.csv’)