"""Collect the total rainfall in a given lat-lon location
over from 1979 to 2010.
"""

import numpy as np

from read_data import extract_data, daily_totals


years = range(1979, 2011)

months = ('01', '02', '03', '04', '05', '06',
          '07', '08', '09', '10', '11', '12')

T = np.zeros((len(years), len(months), 31))

for year_dx in range(len(years)):
    for month in months:
        y = str(years[year_dx])
        data, = extract_data(month, daily_totals, year=y)

        days, _, _ = data.shape
        rf_m = []
        for day in range(days):
            rf = data[day]
            T[year_dx, int(month) - 1, day] = sum(sum(rf[:]))
