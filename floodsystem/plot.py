import matplotlib.pyplot as plt
import matplotlib.dates as date
from datetime import datetime, timedelta
from .analysis import polyfit
import numpy as np

def plot_water_levels(station, dates, levels):
    """Plots water levels of a given station over a given timeframe."""
    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

def plot_water_level_with_fit(station, dates, levels, p, range=False):
    """Plots the water level of a given station in a given timeframe, with a polynomial approximation of order p"""
    x=date.date2num(dates)
    length=len(x)
    # Plot polynomial fit at 30 points along interval (note that polynomial
    # is evaluated using the shift x)
    x1 = np.linspace(x[0], x[-1], 30)
    date_points=date.num2date(x1)
    poly, d0=polyfit(x, levels, p)
    plt.plot(date_points, poly(x1-x[0]))
    
    plt.plot(dates, levels, 'hotpink')
    
    if range==True:
        low=station.typical_range[0]
        high=station.typical_range[1]
        plt.axhline(low, color='r')
        plt.axhline(high, color='r')

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    plt.tight_layout()

    # Display plot
    plt.show()
