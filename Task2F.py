from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def run():
    stations=build_station_list()
    five_s=stations_highest_rel_level(stations, 5)
    dt=2
    for i in range(5):
        next_stat=five_s[i]
        dates, levels=fetch_measure_levels(next_stat.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_level_with_fit(station, dates, levels, 4)

if __name__=="__main__":
    run()
