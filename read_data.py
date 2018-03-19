import numpy as np
import scipy.interpolate as si
from scipy.io.netcdf import NetCDFFile


def daily_totals(rank3tensor):
    shape = np.shape(rank3tensor)
    days = shape[0]/24
    D = np.zeros((days, shape[1], shape[2]))
    for i in range(days):
        for j in range(shape[1]):
            for k in range(shape[2]):
                D[i, j, k] = sum(rank3tensor[l, j, k] for l in range(i*24, (i+1)*24))
    return D

def weekly_max(rank3tensor):
    shape = np.shape(rank3tensor)
    days = shape[0] / 24
    weeks = days / 7
    D = np.zeros((weeks, shape[1], shape[2]))
    for i in range(weeks):
        for j in range(shape[1]):
            for k in range(shape[2]):
                D[i, j, k] = max([rank3tensor[l, j, k] for l in range(i*24*7, (i+1)*24*7)])
    return D


# Show dimensions of data
nc1 = NetCDFFile('data_sorted/CFSR_hourly_rainfall/cold/data1979_01.nc', mmap=False)
# for key in nc1.variables.keys():
#     print(key, np.shape(nc1.variables[key][:]))
# test = daily_totals(nc1.variables['A_PCP_L1_Accum_1'])
# print(test)
# print(np.shape(test))

test2 = weekly_max(nc1.variables['A_PCP_L1_Accum_1'])
print(test2)
print(np.shape(test2))

spring_transition_months = ('04')
warm_months = ('05', '06', '07', '08', '09')
autumn_transition_months = ('10')
cold_months = ('11', '12', '01', '02', '03')
