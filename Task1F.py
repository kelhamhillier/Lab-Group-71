from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations
stations=build_station_list()
p1=stations[0]
print(type(p1.typical_range))
print(sorted(inconsistent_typical_range_stations(stations)))