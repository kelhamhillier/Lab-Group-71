from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import warning

def run():
    stations=build_station_list()
    update_water_levels(stations)
    return warning(stations)

if __name__=="__main__":
    run()
