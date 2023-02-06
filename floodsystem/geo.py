# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
import numpy as np
import math
from haversine import haversine
from .utils import sorted_by_key


def stations_by_distance(stations, p, town=False):
    d=[]
    for i in range(len(stations)):
        p1=stations[i]
        distance=haversine(p, p1.coord)
        if town==False:
            d.append(tuple((p1.name, distance)))
        else:
            d.append(tuple((p1.name, p1.town, distance)))
    return d

def stations_within_radius(stations, centre, r):
    sorted=sorted_by_key(stations_by_distance(stations, centre), 1)
    d=[]
    for i in range(len(sorted)):
        p=sorted[i]
        if p[1]<r:
            d.append(p[0])
        else:
            break
    return d

def rivers_with_station(stations):
    """Returns a set containing a list of all the rivers in the data set with a monitoring station."""
    d = []
    for i in range(len(stations)):
        d.append(stations[i].river)
    return set(sorted(d))


def stations_by_river(stations):
    """Returns a dictionary which maps river names(key) to all the stations which monitor it."""
    a = {}
    for i in range(0, len(stations)):
        a.setdefault(stations[i].river, []).append(stations[i].name)
    return a


def rivers_by_station_number(stations, N):
    """Returns a list of tuples which include river name and number of monitoring stations, sorted in descending order by the number of stations. 
    Input N governs number of rivers shown. In the case that there are more rivers with the same number of stations as the N th entry, these rivers are included in the list"""
    tuples_list = []
    a = stations_by_river(stations)
    for i in range(0, len(stations)):
        b = stations[i].river
        c = (b, len(list(a[b])))
        tuples_list.append(c)
    t = sorted(list(set(tuples_list)))
    t.sort(key=lambda a: a[1], reverse = True)
    p = []
    for i in range (0, N):
        p.append(t[i])
    while t[i+1][1] == t[i][1]:
        p.append(t[i+1])
        i += 1
        if i > len(t) - 2:
            break
    return p
