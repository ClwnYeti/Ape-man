import numpy as np


class GradientDescent:
    def __init__(self, func, step):
        self.func = func
        self.step = step

    @staticmethod
    def do_descent(func, step, e, x_min, x_max, y_min, y_max):
        point = np.array([(x_max + x_min) / 2, (y_max + y_min) / 2])
        lam = step(point[0], point[1])
        grad = GradientDescent._gradient(func, point, e)
        while GradientDescent._length(lam * grad) > e:
            point -= lam * grad
            lam = step(point[0], point[1])
            grad = GradientDescent._gradient(func, point, e)
        return point

    @staticmethod
    def _gradient(func, point, e):
        return [(func(point[0] + e, point[1]) - func(point[0], point[1])) / e,
                (func(point[0], point[1] + e) - func(point[0], point[1])) / e]

    @staticmethod
    def _length(vector):
        return (vector[0]**2 + vector[1]**2)**0.5
