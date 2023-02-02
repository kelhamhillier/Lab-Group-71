import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from .datafetcher import fetch_measure_levels

def plot_water_levels(station, dates, levels):
    t = []
    for i in range(len(dates)):
        x=dates[i]
        t.append(datetime(x))
    plt.plot(t, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("Station A")

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

if __name__=="__main__":
    plot_water_levels()