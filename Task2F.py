from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels

def run():
    stations=build_station_list()
    five_s=floodsystem.flood.stations_highest_rel_level(stations, 5, values=False)
    dt=10
    for i in range(5):
        next_stat=five_s[i]
        dates, levels=floodsystem.datafetcher.fetch_measure_levels(next_stat.measure_id, dt=datetime.timedelta(days=dt), 4)
        floodsystem.plot.plot_water_level_with_fit(next_stat, dates, levels, range=True)

if __name__=="__main__":
    run()
