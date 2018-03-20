%This script calculates total wind in UK in cold season
year = 1979:2010;
month=[1 2 3 11 12];
for i = 1:length(year)
    for j=1:length(month)
        datafile = sprintf('data%d_%02d.nc',year(i),month(j));
        dataU = ncread(datafile,'U_GRD_L103');
        dataV = ncread(datafile,'V_GRD_L103');
        windmag = zeros(size(dataU));
        for k = 1:size(dataU,3)
            windmag(:,:,k) = sqrt(dataU(:,:,k).^2 + dataV(:,:,k).^2);
        end
        tot_time_steps = size(dataU,3);
        total_days = tot_time_steps/24;
        for k = 1:total_days
            cold_wind_data(i,j,k) = sum(sum(sum(windmag(:,:,((k-1)*24+1:k*24)))))/23*23*24; 
        end
    end
end