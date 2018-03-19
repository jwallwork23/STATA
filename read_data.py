import numpy as np
import scipy.interpolate as si
from scipy.io.netcdf import NetCDFFile


years = range(1979, 2011)

spring_transition_months = ('04')
warm_months = ('05', '06', '07', '08', '09')
autumn_transition_months = ('10')
cold_months = ('11', '12', '01', '02', '03')


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

def loop_over_month(month_id, f):
    output = []
    for y in years:
        nc1 = NetCDFFile('data_sorted/CFSR_hourly_rainfall/cold/data'+str(y)+'_'+month_id+'.nc', mmap=False)
        output.append(f(nc1.variables['A_PCP_L1_Accum_1']))
    return output

if __name__ == '__main__':

    # Test daily_totals
    nc1 = NetCDFFile('data_sorted/CFSR_hourly_rainfall/cold/data1979_01.nc', mmap=False)
    for key in nc1.variables.keys():
        print(key, np.shape(nc1.variables[key][:]))
    test = daily_totals(nc1.variables['A_PCP_L1_Accum_1'])
    print(test)
    print(np.shape(test))
    if not bool(input('Test 1: Press 0 to exit, 1 to continue: ')):
        exit(23)

    # Test daily_totals
    test2 = weekly_max(nc1.variables['A_PCP_L1_Accum_1'])
    print(test2)
    print(np.shape(test2))
    if not bool(input('Test 2: Press 0 to exit, 1 to continue: ')):
        exit(23)

    # Tet loop_over_month
    test3 = loop_over_month('01', weekly_max)
    print(test3)
    print(np.shape(test3))
    if not bool(input('Test 3: Press 0 to exit, 1 to continue: ')):
        exit(23)
