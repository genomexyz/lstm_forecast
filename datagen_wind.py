#!/usr/bin/python3

from PyEMD import EMD
import numpy as np
from datetime import datetime, timedelta
import pymongo


#setting
start_year = 2011
end_year = 2019

client = pymongo.MongoClient()
collection = client['sandi_achieve']['metar_param']

all_data = list(collection.find({'stasiun' : 'WAAA'}))
timeseries_wind = []
timeseries_only = []
for i in range(len(all_data)):
	kec_angin = float(all_data[i]['kecepatan_angin']) if all_data[i]['kecepatan_angin'] != 'NO DATA' else -9999
	tahun = '0'+str(all_data[i]['tahun']) if all_data[i]['tahun'] < 10 else str(all_data[i]['tahun'])
	bulan = '0'+str(all_data[i]['bulan']) if all_data[i]['bulan'] < 10 else str(all_data[i]['bulan'])
	hari = '0'+str(all_data[i]['hari']) if all_data[i]['hari'] < 10 else str(all_data[i]['hari'])
	jam = '0'+str(all_data[i]['jam']) if all_data[i]['jam'] < 10 else str(all_data[i]['jam'])
	menit = '0'+str(all_data[i]['menit']) if all_data[i]['menit'] < 10 else str(all_data[i]['menit'])
#	print('%s%s%s%s%s'%(tahun, bulan, hari, jam, menit), kec_angin)
	timeseries_wind.append(kec_angin)
	timeseries_only.append('%s%s%s%s%s'%(tahun, bulan, hari, jam, menit))

print(timeseries_only)

#fill missing data
year_current = start_year
waktu_gen = datetime(year_current, 1, 1, 0, 0)
real_timeseries_wind = []
while year_current < end_year:
	print(waktu_gen)
	waktu_gen += timedelta(minutes=30)
	#strtime example: 2019-01-01 00:00:00
	waktu_gen_str = waktu_gen.strftime('%Y%m%d%H%M')
	print(waktu_gen_str)
	try:
		idx = timeseries_only.index(waktu_gen_str)
		#real_timeseries_wind.append([waktu_gen_str, timeseries_wind[idx]])
		real_timeseries_wind.append(timeseries_wind[idx])
	except ValueError:
		real_timeseries_wind.append(-9999)
	year_current = int(waktu_gen.strftime('%Y'))
print(len(real_timeseries_wind))
print(len(timeseries_wind))

real_timeseries_wind = np.asarray(real_timeseries_wind)
np.save('timeseries_data_full.npy', real_timeseries_wind)
