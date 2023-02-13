from floodsystem.analysis import polyfit
import numpy as np

a=60

input_poly=np.poly1d([3, 4, 5])
x = np.linspace(a, a+20, 101)
y = input_poly(x)
output_poly, d0=polyfit(x, y, 2)
assert d0==a
for i in range(0, 100, 11):
    x=round(input_poly(i), 5)
    y=round(output_poly(i-a), 5)
    assert x==y