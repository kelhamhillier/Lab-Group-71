from .datafetcher import fetch_measure_levels
import datetime
def stations_level_over_threshold(stations, tol):
    a = []
    for station in stations:
        if station.relative_water_level() == None:
            b = []
        elif station.relative_water_level() > tol:
            a.append((station, station.relative_water_level()))
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

def gradient_of_water_level(stations, dt):
    """Arbritrary number of hours tracked, if water level increases by x amount in y hours, 
    assign gradient level 1 or 2, if it decreases then assign gradient -1"""
    tuple_list = []
    for j in range(0, len(stations)):
        station = stations[j]
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(hours=dt))
        if levels == []:
            tuple_list.append((station.name, "unavailable"))
        else:
            if levels[0] - min(levels) > 0.1:
                a = "grad_+2"
            elif levels[0] - min(levels) > 0.03:
                a = "grad_+1"
            elif max(levels) - levels[0] > 0.03:
                a = "grad_-1"
            else:
                a = "grad_0"
            tuple_list.append((station.name, a))
    """Returns a list of station names and their current gradient level"""
    return(tuple_list)

def warning(stations):
    """Two values of relative water level selected: 0.8, 1.2, these values can be altered.
    Any rivers with a relative water level above 0.8 is given a flood warning rating, low to severe, and below this it is assumed as no risk.
    If the water level is above 1.2 and rising, represents a severe risk of flood.
    If the level is above 0.8 and rising quickly i.e. has a gradient of grad_+2, it also represents a severe risk.
    The other risk evaluations are then made in similar fashion based on their water level and gradient
    All values chosen can be altered to better reflect real world situations."""

    print("Running, this may take a second") #program can take a few seconds to produce results, this just indicates the program is running
    dt = 6
    a = stations_level_over_threshold(stations, 0.8)
    b = []
    for i in range(0, len(a)):
        b.append(a[i][0])
    c = gradient_of_water_level(b, dt)
    severe_risk = []
    high_risk = []
    moderate_risk = []
    low_risk = []
    for j in range(0, len(c)):
        if b[j].relative_water_level() > 1.2 and c[j][1] == "grad_+2" or "grad_+1":
            severe_risk.append(b[j].town)
        elif b[j] > 1.2 or c[j][1] == "grad_+2":
            high_risk.append(b[j].town)
        elif c[j][1] == "grad_-1":
            low_risk.append(b[j].town)
        else:
            moderate_risk.append(b[j].town)
    return print(f"The following towns are at severe risk of flooding {severe_risk}")
