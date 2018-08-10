from pathlib import Path

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

pos_data_fp = Path('pos data for weka.csv')
neg_data_fp = Path('neg data for weka.csv')

pos_data = pd.read_csv(str(pos_data_fp.resolve()))
neg_data = pd.read_csv(str(neg_data_fp.resolve()))

pos_data = pos_data.dropna()
neg_data = neg_data.dropna()
scaler = MinMaxScaler((-1, 1))

print(pos_data.values.max(axis=0))
print(neg_data.values.max(axis=0))
print(pos_data.values.min(axis=0))
print(neg_data.values.min(axis=0))

pos_data_scaled = pd.DataFrame(scaler.fit_transform(pos_data),
                               columns=pos_data.columns)
neg_data_scaled = pd.DataFrame(scaler.fit_transform(neg_data),
                               columns=neg_data.columns)

pos_data_scaled_fp = Path('scaled pos data.csv')
neg_data_scaled_fp = Path('scaled neg data.csv')
pos_data_scaled.to_csv(str(pos_data_scaled_fp.resolve()))
neg_data_scaled.to_csv(str(neg_data_scaled_fp.resolve()))
