#download necessary libraries (use install.packages command to download necessary packages)
library(extRemes) #install.packages("extRemes")
library(xts) #install.packages("xts")
library(evir) #install.packages("evir")

#Peaks over Threshold method

#daily totals for sum. Change file paths as necessary
dtots <- read.csv("~/Downloads/daily_totals_r_gp11-11_warm.csv",header=TRUE)
#turn matrix into vectors
dt_sum <- unlist(dtots)

#fit a GPD to data for specific threshold (can try with different thresholds)
fit_gpd_sum <- fevd(dt_sum,method="MLE",threshold=29,type="GP")
plot(fit_gpd_sum,type="qq",main="Summer Daily Totals, Threshold=29") #look at this to tune threshold based on fit to line


#daily totals of winter
dt_winter <- read.csv("~/Downloads/Untitled_message/daily_totals_r_gp11-11_cold_takeMax=False.csv",header=TRUE)
dtw <- unlist(dt_winter)

#fiting GPD to winter daily totals for specific threshold (tune appropriately)
fit_gpd_win <- fevd(dtw,method="MLE",threshold=29,type="GP")
plot(fit_gpd_win,type="qq",main="Winter Daily Totals, Threshold=29")

#results
fit_gpd_win #see shape 

#set location to be threshold, shape and scale are from the fitting results results above
shape = -0.4473
scale = 10.749

#high quantile
qgpd(p=0.9999,xi=shape,beta=scale,mu=29) #location is set to be threshold chosen

#since shape negative, endpoint
qgpd(p=1,xi=shape,beta=scale,mu=29)

#acf to see about correlation for independence criteria. Shows serial dependence
acf(dtw)
acf(dt_sum)


#Block maxima Method

#weakly maxima of daily totals
wm_win <- read.csv("~/Downloads/Untitled_message/weekly_max_r_gp11-11_cold.csv",header=TRUE)
wm_sum <- read.csv("~/Downloads/Untitled_message/weekly_max_r_gp11-11_warm.csv",header=TRUE)

#acf for weekly maxima. Shows less dependence

#fit GEV
fit_gev_sum <- fevd(unlist(wm_sum),method="MLE",type="GEV")
fit_gev_win <- fevd(unlist(wm_win),method="MLE",type="GEV")

#again get high quantile (for summer)
fit_gev_sum

location =  1.33 #(from location)
shape =  0.18
scale = 0.99

qgev(p=0.9999, xi=shape,sigma=1/scale,mu=location)
