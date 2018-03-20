import pandas as pd
import numpy as np

def take_ratio(season, field, location):
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

take_ratio('warm', 'r', (11, 11))
take_ratio('cold', 'r', (11, 11))
