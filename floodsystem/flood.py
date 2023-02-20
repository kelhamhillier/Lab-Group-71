from .station import MonitoringStation
def stations_level_over_threshold(stations, tol):
    a = []
    for station in stations:
        if station.relative_water_level() == None:
            b = []
        elif station.relative_water_level() > tol:
            a.append((station.name, station.relative_water_level()))
    a.sort(key=lambda c: c[1], reverse = True)
    return a

def stations_highest_rel_level(stations, N):
    a = []
    for station in stations:
        if station.relative_water_level() == None:
            b = []
        else:
            a.append((station.name, station.relative_water_level()))
    a.sort(key=lambda a: a[1], reverse = True)
    c = []
    for i in range(0, N):
        c.append(a[i])
    return c
