from floodsystem.analysis import polyfit
import numpy as np

input_poly=np.poly1d([3, 4, 5])
x = np.linspace(0, 10, 101)
y = input_poly(x)
output_poly, d0=polyfit(x, y, 2)
for i in range(0, 100, 10):
    x=round(input_poly(i), 5)
    y=round(output_poly(i), 5)
    assert x==y