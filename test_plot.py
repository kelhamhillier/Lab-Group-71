from floodsystem.plot import plot_water_level_with_fit, plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import datetime

stations=build_station_list()
station=stations[123]
dt=2
dates, levels = fetch_measure_levels(
        station.measure_id, dt=datetime.timedelta(days=dt))
plot_water_levels(station, dates, levels)