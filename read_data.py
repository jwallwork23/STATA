import numpy as np
from scipy.io.netcdf import NetCDFFile


years = range(1979, 2011)


def extract_data(month_id, func, year=None):
    if month_id in ('11', '12', '01', '02', '03'):
        season = "cold/"
    elif month_id == '04':
        season = "spring_transition/"
    elif month_id == '10':
        season = "autumn_transition/"
    else:
        season = "warm/"

    output = []
    di = 'data_sorted/CFSR_hourly_rainfall/' + str(season)
    if year is None:
        for y in years:
            f = di + 'data' + str(y) + '_' + str(month_id) + '.nc'
            nc1 = NetCDFFile(f, mmap=False)
            output.append(func(nc1.variables['A_PCP_L1_Accum_1']))
    else:
        f = di + 'data' + str(year) + '_' + str(month_id) + '.nc'
        nc1 = NetCDFFile(f, mmap=False)
        output.append(func(nc1.variables['A_PCP_L1_Accum_1']))

    return output


def daily_totals(rank3tensor):
    shape = np.shape(rank3tensor)
    days = int(shape[0]/24)
    D = np.zeros((days, shape[1], shape[2]))
    for i in range(days):
        for j in range(shape[1]):
            for k in range(shape[2]):
                D[i, j, k] = sum(rank3tensor[l, j, k]
                                 for l in range(i*24, (i+1)*24))
    return D


def weekly_max(rank3tensor):
    shape = np.shape(rank3tensor)
    days = int(shape[0] / 24)
    weeks = int(days / 7)
    D = np.zeros((weeks, shape[1], shape[2]))
    for i in range(weeks):
        for j in range(shape[1]):
            for k in range(shape[2]):
                D[i, j, k] = max([rank3tensor[l, j, k]
                                  for l in range(i*24*7, (i+1)*24*7)])
    return D

# output0 = extract_data('04', weekly_max, year="1980")
# output1 = extract_data('04', daily_totals, year="1980")
# print(output0[0])
# print(output1[0])
