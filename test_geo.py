import floodsystem.geo
from floodsystem.station import MonitoringStation
from haversine import haversine
def test_stations_by_distance():
    a = MonitoringStation("N/A", "N/A", "House A", (-1.0, 0.1), None, "N/A", "Town A")
    b = MonitoringStation("N/A", "N/A", "House B", (5.0, 2.0), None, "N/A", "Town B")
    c = MonitoringStation("N/A", "N/A", "House C", (1.0, 0.0), None, "N/A", "Town C")
    list=[a, b, c]
    assert floodsystem.geo.stations_by_distance(list, (0, 0))==[(a.name, haversine((a.coord), (0,0))), (b.name, haversine((b.coord), (0,0))), (c.name, haversine((c.coord), (0,0)))]
    assert floodsystem.geo.stations_by_distance(list, (5.0, 2.0), town=True)==[(a.name, a.town, haversine((a.coord), (5.0, 2.0))), (b.name, b.town, haversine((b.coord), (5.0, 2.0))), (c.name, c.town, haversine((c.coord), (5.0, 2.0)))]

def test_stations_within_radius():
    a = MonitoringStation("N/A", "N/A", "House A", (-1.0, 0.1), None, "N/A", "Town A")
    b = MonitoringStation("N/A", "N/A", "House B", (5.0, 2.0), None, "N/A", "Town B")
    c = MonitoringStation("N/A", "N/A", "House C", (1.0, 0.0), None, "N/A", "Town C")
    list=[a, b, c]
    assert floodsystem.geo.stations_within_radius(list, (0,0), 100)==[]
    assert floodsystem.geo.stations_within_radius(list, (0,0), 200)==[c.name, a.name]
    assert floodsystem.geo.stations_within_radius(list, (0,0), 1000)==[c.name, a.name, b.name]

if __name__=="__main__":
    test_stations_by_distance()
    test_stations_within_radius()