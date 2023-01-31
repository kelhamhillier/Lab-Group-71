# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from .stationdata import build_station_list
import numpy as np
import math
from haversine import haversine
from .utils import sorted_by_key

stations=build_station_list()

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


