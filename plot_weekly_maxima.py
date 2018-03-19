import matplotlib.pyplot as plt
import numpy as np
import read_data


years = range(1979, 2011)
i_years = range(len(years))
# months = ('11', '12', '01', '02', '03')
months = ('05', '06', '07', '08', '09')

for y in i_years:
    dat_y = ()
    for m in months:
        dat_y += tuple(read_data.extract_data(m, read_data.weekly_max, years[y])[0][:, 11, 11])
    print(dat_y)
    plt.plot(range(1,21), dat_y)
    plt.title('Year '+str(years[y]))
    plt.xlabel('Week')
    plt.ylabel('Weekly max rainfall')
    plt.show()
    exit(23)
