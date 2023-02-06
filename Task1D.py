from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list
def run():
    stations=build_station_list()

    def river_with_mon_stats(stations):
        a = sorted(rivers_with_station(stations))
        b = []
        for i in range(0,10):
            b.append(a[i])
        print(f"{len(a)} stations. First 10 - {b}")

    def stations_on_river(x):
        print(sorted(stations_by_river(stations)[x]))
    return river_with_mon_stats(stations), print("\n"), stations_on_river("River Aire"), print("\n"), stations_on_river("River Cam"), print("\n"), stations_on_river("River Thames")
    
if __name__=="__main__":
    run()
