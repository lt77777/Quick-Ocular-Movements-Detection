"""Helper functions for facemesh.py"""
import numpy as np

def distance(p1, p2):
    """Takes two points in R^2 and returns the distance between them."""
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def square(x):
    """Takes a number and returns the square of that number."""
    return x**2

def polygon_area(points):
    """Takes a list of points in R^2 and returns the 
    area of the polygon using shoelace formula
    """
    x = []
    y = []
    for i in points:
        x.append(i[0])
        y.append(i[1])
    correction = x[-1] * y[0] - y[-1]* x[0]
    main_area = np.dot(x[:-1], y[1:]) - np.dot(y[:-1], x[1:])
    return 0.5*np.abs(main_area + correction)

def intersect(p1, p2, p3, p4):
    """Takes four points in R^2 and returns the intersection
    of the two lines defined by the points.
    """
    line1 = [p1, p2]
    line2 = [p3, p4]
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return [x, y]
