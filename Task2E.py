from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def run():
    stations=build_station_list()
    five_s=floodsystem.flood.stations_highest_rel_level(stations, 5, values=False)
    dt=10
    for i in range(5):
        next_stat=five_s[i]
        dates, levels=floodsystem.datafetcher.fetch_measure_levels(next_stat.measure_id, dt=datetime.timedelta(days=dt))
        floodsystem.plot.plot_water_levels(next_stat, dates, levels)

if __name__=="__main__":
    run()
