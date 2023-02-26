from floodsystem.plot import plot_water_level_with_fit, plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime

stations=build_station_list()
plot_station=stations[146]
update_water_levels(stations)

#for station in stations:
#    if station.name=="Sheffield Carr Brook Screen":
#        plot_station=station
#        break

dt=200
dates, levels = fetch_measure_levels(
        plot_station.measure_id, dt=datetime.timedelta(days=dt))
plot_water_levels(plot_station, dates, levels)
plot_water_level_with_fit(plot_station, dates, levels, 4)