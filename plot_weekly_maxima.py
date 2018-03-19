import matplotlib.pyplot as plt

import read_data


years = range(1979, 2011)
i_years = range(len(years))
# months = ('11', '12', '01', '02', '03')
months = ('05', '06', '07', '08', '09')

for y in i_years:
    dat_y = ()
    for m in months:
        dat_y += tuple(read_data.loop_over_month(m, read_data.weekly_max))
    plt.plot(range(len(dat_y)), dat_y[y][ :, 11, 11])
    plt.title('Year '+y)
    plt.xlabel('Week')
    plt.ylabel('Weekly max rainfall')
    plt.show()
    exit(23)
