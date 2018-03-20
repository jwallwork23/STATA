%This script calculates total daily precipitation in UK in warm season
year = 1979:2010;
month=5:9
for i = 1:length(year)
    for j=1:length(month)
        datafile = sprintf('data%d_%02d.nc',year(i),month(j));
        data = ncread(datafile,'A_PCP_L1_Accum_1');
        tot_time_steps = size(data,3);
        total_days = tot_time_steps/24;
        for k = 1:total_days
            warm_pcp_data(i,j,k) = sum(sum(sum(data(:,:,((k-1)*24+1:k*24))))); 
        end
    end
end