#!/usr/bin/python

from PyEMD import EMD
from datetime import datetime, timedelta
import numpy as np
import pymongo

#setting
wind_data_filename = 'timeseries_data_full.npy'
timeseries_param_len = 18
timeseries_label_len = 1

timeseries = np.load(wind_data_filename, allow_pickle=True)

print(timeseries)
