import numpy
import json
import matplotlib.pyplot as plt

def calculate(v1, v2, v3, s):
    # take (in order): x1, x2, x3, t
    return ((1 - s)**2) * v1 + 2 * s * (1 - s) * v2 + (s**2) * v3

def plot_function(data, ts, title="Wykres funkcji"):
    for d in data:
        control_points, x_coordinates, y_coordinates = [], [], []
        for t in ts:
            x = calculate(float(d['p1'][0]), float(d['p2'][0]), float(d['p3'][0]), t)
            y = calculate(float(d['p1'][1]), float(d['p2'][1]), float(d['p3'][1]), t)
            x_coordinates.append(x)
            y_coordinates.append(y)
        color = d['color']
        print(color, d['color'])
        control_points.append(d['p1'])
        control_points.append(d['p2'])
        control_points.append(d['p3'])
        plt.plot(x_coordinates, y_coordinates, color=color)
        for point in control_points:
            plt.scatter(point[0], point[1], color=color)
    plt.title(title)
    plt.xlabel("Oś X")
    plt.ylabel("Oś Y")
    plt.grid(True)
    plt.show()


json_file_path = 'C:/Users/48512/Desktop/python_projects/winter23/found_online/9/plik.json'

# Open the file and load the JSON content
with open(json_file_path, 'r') as file:
    list_from_file = json.load(file)

NUMBER_OF_POINTS = 250

ts = [float(x) for x in numpy.linspace(0, 1, num=NUMBER_OF_POINTS)]

plot_function(list_from_file, ts)