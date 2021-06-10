import math
import numpy as np
def funcx(x):
    return np.log(x**3 - x**2 +2 )

a , b = 0.4, 1.6

epsilon = 1e-2
x =0.5
xant = x

x = funcx(x)
print(xant-x)

while (((x%100000000)-(xant%100000000))%100000000)> epsilon:
    xant = x
    x = funcx(x)
    print(xant-x)