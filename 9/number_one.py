import numpy
import random
import math
import matplotlib.pyplot as plt

def calculate(v1, v2, r, s):
    # take (in order): r1, r2, t, d
    # give (in order): x, y
    return (v2 - v1) * math.cos(r) + s * math.cos((v2 - v1) * r / v1), (v2 - v1) * math.sin(r) - s * math.sin((v2 - v1) * r / v1)

def compute_lcm(x, y):

   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

def plot_function(x_coordinates, y_coordinates, title="Wykres funkcji"):
    plt.plot(x_coordinates, y_coordinates)
    plt.title(title)
    plt.xlabel("Oś X")
    plt.ylabel("Oś Y")
    plt.grid(True)
    plt.show()

r1 = random.randrange(1,10)
r2 = random.randrange(1,10)
d = random.randrange(1,10)

NUMBER_OF_POINTS = 250

m = 2 * math.pi * compute_lcm(r1, r2) / r2

ts = list(numpy.linspace(0, m, num=NUMBER_OF_POINTS))

xs, ys = [], []

for t in ts:
    x, y = calculate(r1, r2, t, d)
    xs.append(x)
    ys.append(y)

plot_function(xs, ys, title=f"Wykres funkcji r1={r1}, r2={r2} i d={d}")