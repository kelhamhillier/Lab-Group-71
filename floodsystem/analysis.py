import matplotlib.dates as plt
import numpy as np
import datetime

def polyfit(dates, levels, p):
    """Returns a polynomial approximation of order p for the dataset (dates, levels), along with the timeshift across the x axis."""
    if dates[5]==datetime.datetime:
        print("datetime.datetime recognised")
        dates=plt.date2num(dates)
    # Find coefficients of best-fit polynomial f(dates) of degree p
    p_coeff = np.polyfit(dates-dates[0], levels, p)

    # Convert coefficient into a polynomial that can be evaluated,
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)
    return poly, dates[0]