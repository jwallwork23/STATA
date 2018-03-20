"""A simple plotting script for finding the weekly maximum
rainfall from 1979 to 2010. This code requires specifying a
specific lat-lon location.
"""

import matplotlib.pyplot as plt

from read_data import *


years = range(1979, 2011)
i_years = range(len(years))
months = ('11', '12', '01', '02', '03') if input('0: warm, 1: cold ') else ('05', '06', '07', '08', '09')

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rc('legend', fontsize='x-large')

for y in i_years:
    dat_y = ()
    lat = 11
    lon = 11
    for m in months:
        dat_y += tuple(extract_data(m, weekly_max,
                                    'r', year=years[y])[0][:, lat, lon])
    plt.plot(range(1, 21), dat_y)
    plt.title('Year '+str(years[y]))
    plt.xlabel('')
    plt.xticks(range(2, 21, 4), ('May', 'June', 'July', 'August', 'September'))
    plt.ylabel(r'Weekly max rainfall ($kg\,m^{-2}$)')
    plt.savefig('plots/weekly_max_rainfall_'+str(years[y])+'.png')
    plt.clf()
