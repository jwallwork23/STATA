from read_data import *

import pandas as pd

years = range(1979, 2011)


def write_weekly_maximums(season, field, location):
    if not isinstance(location, tuple):
        raise ValueError("location should be a tuple (x, y)")

    x, y = location

    if season == "warm":
        months = ('05', '06', '07', '08', '09')
    elif season == "cold":
        months = ('11', '12', '01', '02', '03')
    else:
        raise ValueError("Season not recognized")

    if field != "r":
        raise NotImplementedError("Only rain implemented at the moment")

    data = {}
    for year in years:
        print("Extracting %s season data for year %d..." % (season, year))
        key = "%s" % str(year)
        data[key] = ()
        for month in months:
            data[key] += tuple(extract_data(month, weekly_max,
                                            "r", year=year)[0][:, x, y])
    print('Done!')

    # Acknowledge that winter crosses the New Year!
    if season == "cold":
        for key in data:
            key += '-' + str(int(key)+1)

    df = pd.DataFrame(data)
    result = "weekly_max_%s_gp%s-%s_%s.csv" % (field, x, y, season)
    df.to_csv(result, index=False, mode="w")


def write_daily_totals(season, field, location, takeMax=False):
    if not isinstance(location, tuple):
        raise ValueError("location should be a tuple (x, y)")

    x, y = location

    if season == "warm":
        months = ('05', '06', '07', '08', '09')
    elif season == "cold":
        months = ('11', '12', '01', '02', '03')
    else:
        raise ValueError("Season not recognized")

    if field != "r":
        raise NotImplementedError("Only rain implemented at the moment")

    data = {}
    for year in years:
        print("Extracting %s season data for year %d..." % (season, year))
        key = "%s" % str(year)
        data[key] = ()
        for month in months:
            if takeMax:
                monthDat = extract_data(month, daily_totals, "r", year=year)[0][:, x, y]
                tup = tuple(max(monthDat[7*i:7*(i+1)]) for i in range(4))
            else:
                tup = tuple(extract_data(month, daily_totals, "r", year=year)[0][:, x, y])
            data[key] += tup
    print('Done!')

    # Acknowledge that winter crosses the New Year!
    if season == "cold":
        for key in data:
            key += '-' + str(int(key) + 1)

    df = pd.DataFrame(data)
    result = "daily_totals_%s_gp%s-%s_%s_takeMax=%s.csv" % (field, x, y, season, takeMax)
    df.to_csv(result, index=False, mode="w")


# write_weekly_maximums("cold", "r", (11, 11))
write_daily_totals("warm", "r", (11, 11), takeMax=True)
write_daily_totals("cold", "r", (11, 11), takeMax=True)
