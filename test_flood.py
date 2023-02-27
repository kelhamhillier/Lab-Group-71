from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level, gradient_of_water_level, warning
from floodsystem.stationdata import build_station_list, update_water_levels

stations = build_station_list()

update_water_levels(stations)
test_stations = []
for i in range(0, 8):
    test_stations.append(stations[i])
tol = 0.2
N = 2
dt = 4
def test_stations_level_over_threshold():
    return print(stations_level_over_threshold(test_stations, tol))

def test_stations_highest_rel_level():
    return print(stations_highest_rel_level(test_stations, N))
def test_gradient_of_water_level():
    return print(gradient_of_water_level(test_stations, dt))
def test_warning():
    return warning(test_stations)

if __name__=="__main__":
    test_stations_level_over_threshold()
    test_stations_highest_rel_level()
    test_gradient_of_water_level()
    test_warning()
