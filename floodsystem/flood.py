def stations_level_over_threshold(stations, tol):
    a = []
    for station in stations:
        if relative_water_level(station) == None:
            b = []
        elif relative_water_level(station) > tol:
            a.append((station.name, relative_water_level(station)))
    a.sort(key=lambda c: c[1], reverse = True)
    return a

def stations_highest_rel_level(stations, N):
    a = []
    for station in stations:
        if relative_water_level(station) == None:
            b = []
        else:
            a.append((station.name, relative_water_level(station)))
    a.sort(key=lambda a: a[1], reverse = True)
    c = []
    for i in range(0, N):
        c.append(a[i])
    return c
