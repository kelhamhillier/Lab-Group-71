from floodsystem.stationdata import build_station_list

from floodsystem.utils import sorted_by_key
from floodsystem.geo import stations_by_distance


stations=build_station_list()

def closest_by_distance(stations, p, town=False):
    if town==False:
        sorted=sorted_by_key(stations_by_distance(stations, p), 1)
    else:
        sorted=sorted_by_key(stations_by_distance(stations, p, town=True), 2)
    return sorted[:10]
    
def furthest_by_distance(stations, p, town=False):
    if town==False:
        sorted=sorted_by_key(stations_by_distance(stations, p), 1)
    else:
        sorted=sorted_by_key(stations_by_distance(stations, p, town=True), 2)
    return sorted[-10:]
 
print("Closest 10 stations are:",closest_by_distance(stations, (52.2053, 0.1218), town=True))
print("Furthest 10 stations are:",furthest_by_distance(stations, (52.2053, 0.1218), town=True))