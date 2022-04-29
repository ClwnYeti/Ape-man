import math

import numpy as np
from StepGoldenRatio import StepGoldenRatio


class FletcherReeves:
    def __init__(self, func, step):
        self.func = func
        self.step = step

    def do(self, e, start_point):
        return FletcherReeves.do_descent(self.func, self.step, e, start_point)

    @staticmethod
    def do_descent(func, step, e, start_point):
        iteration = 0
        x, y = start_point[0], start_point[1]
        x_next, y_next = x, y
        grad_norm, grad_norm_pr = 0, 0
        points = []
        point = np.array(start_point)
        points.append(point.copy())
        while True:
            f = func(x, y)
            next_point = np.array(x_next, y_next)
            points.append(next_point.copy())
            if grad_norm_pr == 0 or (iteration + 1) % 3 == 0:
                beta = 0
                grad_point = np.array(x, y)
                p_x_pr = -FletcherReeves._gradient(func, grad_point, e)[0]
                p_y_pr = -FletcherReeves._gradient(func, grad_point, e)[1]
            else:
                beta = grad_norm ** 2 / grad_norm_pr ** 2
            iteration += 1
            grad_point = np.array(x, y)
            grad_x = FletcherReeves._gradient(func, grad_point, e)[0]
            grad_y = FletcherReeves._gradient(func, grad_point, e)[1]
            grad_norm = math.sqrt(grad_x ** 2 + grad_y ** 2)
            lamb = methopt(func, x, y, grad_x, grad_y, a, b, eps)
            x_next = x + lamb * p_x_pr
            y_next = y + lamb * p_y_pr
            grad_point = np.array(x_next, y_next)
            p_x = - FletcherReeves._gradient(func, grad_point, e)[0] + beta * p_x_pr
            p_y = - FletcherReeves._gradient(func, grad_point, e)[1] + beta * p_y_pr
            f_next = func(x_next, y_next)
            if abs(x - x_next) / 2 < e and abs(y - y_next) / 2 < e or abs(grad_x) < e and abs(
                    grad_y) < e or abs(f_next - f) / 2 < e:
                break
            x, y = x_next, y_next
            p_x_pr, p_y_pr = p_x, p_y
            grad_norm_pr = grad_norm
        print(iteration - 1)
        # draw(a, b, func, points_x, points_y, 'метод сопряжённых градиентов')
        return iteration, point, points

    @staticmethod
    def _gradient(func, point, e):
        return np.array([(func([point[j] + e if j == i else point[j] for j in range(len(point))]) - func(point)) / e
                         for i in range(len(point))])
