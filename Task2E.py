from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def run():
    stations=build_station_list()
    update_water_levels(stations)
    five_s=stations_highest_rel_level(stations, 5)
    dt=10
    for i in range(5):
        next_stat=five_s[i]
        for station in stations:
            if station.name==next_stat[0]:
                next_stat=station
                dates, levels=fetch_measure_levels(next_stat.measure_id, dt=datetime.timedelta(days=dt))
                plot_water_levels(next_stat, dates, levels)
                break

if __name__=="__main__":
    run()
