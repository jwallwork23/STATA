import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from read_data import *

years = range(1979, 2011)


def take_ratio(season, field, location):
    """Computes a ratio of field intensity
    given a particular season, field (i.e. rainfall)
    and location (x, y) - lat-lon location.

    :arg season: A string denoting the season. Supported seasons
                 are "warm" and "cold".
    :arg field: A field to examine. Rainfall is dentoted by "r",
                wind speed components are 'u', 'v'.
    :arg location: A tuple denoting the grid point locations (x, y).
    """

    x, y = location

    dataDaily = pd.read_csv('daily_totals_%s_gp%d-%d_%s_takeMax=True.csv' % (field, x, y, season))
    dataHourly = pd.read_csv('weekly_max_%s_gp%d-%d_%s.csv' % (field, x, y, season))

    dailyDict = dataDaily.to_dict()
    hourlyDict = dataHourly.to_dict()

    ratio = {}

    for year in dailyDict:
        ratio[str(year)] = []
        for weeks in dailyDict[year]:
            vday = dailyDict[year][weeks]
            vhr = hourlyDict[year][weeks]
            try:
                ratio[str(year)].append(vday / vhr)
            except:
                ratio[str(year)].append(np.nan)

    # import ipdb; ipdb.set_trace()
    df = pd.DataFrame(ratio)
    result = "ratio_%s_gp%s-%s_%s.csv" % (field, x, y, season)
    df.to_csv(result, index=False, mode="w")


def get_ratio(season, field, location):
    x, y = location

    if season == "warm":
        months = ('05', '06', '07', '08', '09')
    elif season == "cold":
        months = ('11', '12', '01', '02', '03')
    else:
        raise ValueError("Season not recognized")

    if field != "r":
        raise NotImplementedError("Only rain implemented at the moment")

    hourlyMax = 0
    dailyMax = 0
    for year in years:
        # print("Extracting %s season data for year %d..." % (season, year))
        for month in months:
            hly = max(extract_data(month, weekly_max,
                                   "r", year=year)[0][:, x, y])
            dly = max(extract_data(month, daily_totals,
                                   "r", year=year)[0][:, x, y])
            if hly > hourlyMax:
                hourlyMax = hly
            if dly > dailyMax:
                dailyMax = dly
    # print('Hourly maximum at %d-%d: %f' % (x, y, hourlyMax))
    # print('Daily maximum at %d-%d: %f' % (x, y, dailyMax))

    return hourlyMax, dailyMax

locations = ((11, 11), (11, 12), (12, 12), (13, 13),
             (13, 14), (14, 14), (14, 16), (15, 16), (16, 16))

H = []
D = []
for x, y in locations:
    h, d = get_ratio('warm', 'r', (x, y))
    H.append(h)
    D.append(d)
    print('Ratio %d-%d: %f, hourly: %f, daily: %f' % (x, y, d/h, h, d))
plt.scatter(H, D)
plt.xaxis('Hourly max')
plt.yaxis('Daily max')
plt.savefig('ratios.pdf')
