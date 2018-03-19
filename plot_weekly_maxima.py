import matplotlib.pyplot as plt
import numpy as np
import read_data


years = range(1979, 2011)
i_years = range(len(years))
# months = ('11', '12', '01', '02', '03')
months = ('05', '06', '07', '08', '09')

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rc('legend', fontsize='x-large')

for y in i_years:
    dat_y = ()
    for m in months:
        dat_y += tuple(read_data.extract_data(m, read_data.weekly_max, 'r', year=years[y])[0][:, 11, 11])
    plt.plot(range(1,21), dat_y)
    plt.title('Year '+str(years[y]))
    plt.xlabel('Week')
    plt.xticks(range(2, 21, 4), ('May', 'June', 'July', 'August', 'September'))
    plt.ylabel(r'Weekly max rainfall ($kg\,m^{-2}$)')
    plt.savefig('plots/weekly_max_rainfall_'+str(years[y])+'.png')
    plt.clf()
