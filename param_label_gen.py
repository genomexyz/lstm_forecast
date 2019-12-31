#!/usr/bin/python3

from PyEMD import EMD
from datetime import datetime, timedelta
import numpy as np
import pymongo

#setting
wind_data_filename = 'timeseries_data_full.npy'

wind_data = np.load(wind_data_filename)
print(wind_data)
print(np.shape(wind_data))
