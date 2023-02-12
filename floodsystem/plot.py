import matplotlib.pyplot as plt
import matplotlib.dates as dates
from datetime import datetime, timedelta
from .analysis import polyfit
import numpy as np

def plot_water_levels(station, dates, levels):
    t = []
    for i in range(len(dates)):
        x=dates[i]
        t.append(x)
    plt.plot(t, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

def plot_water_level_with_fit(station, dates, levels, p, range=False):
    x=dates.dates2num(dates)
    plt.plot(x, levels, '.')

    # Plot polynomial fit at 30 points along interval (note that polynomial
    # is evaluated using the shift x)
    x1 = np.linspace(x[0], x[-1], 30)
    poly, d0=polyfit(dates, levels, p)
    plt.plot(x1, poly(x1 - x[0]))
    if range==True:
        low=station.typical_range[0]
        high=station.typical_range[1]
        plt.plot(x, low)
        plt.plot(x, high)

    # Display plot
    plt.show()

if __name__=="__main__":
    plot_water_levels()