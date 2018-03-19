import matplotlib.pyplot as plt
import numpy as np

import read_data


years = range(0, 5)
months = ('11', '12', '01', '02', '03')

for y in years:
    for m in months:
        dat = read_data.loop_over_month(m, read_data.weekly_max)
        print(dat[0])
        plt.plot([1,2,3,4], dat[y][ :, 11, 11])
        plt.xlabel('Week')
        plt.ylabel('Weekly max rainfall')
        plt.show()
