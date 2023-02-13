import matplotlib.dates as plt
import numpy as np

def polyfit(dates, levels, p):
    if type(dates[50]) == "datetime.datetime":
        x = plt.date2num(dates)
    else:
        x = dates
    # Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(x - x[0], levels, p)

    # Convert coefficient into a polynomial that can be evaluated,
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)
    return poly, x[0]