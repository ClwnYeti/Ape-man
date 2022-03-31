import math


class Dichotomy:
    def __init__(self, func):
        self._func = func

    @staticmethod
    def do_method(func, left, right, e):
        i = 0
        while abs(right - left) > e:
            i += 1
            middle = (right + left) / 2
            fml = func(middle - e / 2)
            fmr = func(middle + e / 2)
            if (fml < fmr) > 0:
                right = middle
            else:
                left = middle
        return (left + right) / 2, i, right - left

    def do(self, left, right, e):
        return Dichotomy.do_method(self._func, left, right, e)


print(Dichotomy.do_method((lambda x: x**2 * math.e ** math.sin(x)), -math.pi + 0.00001, math.pi, 0.00001))

