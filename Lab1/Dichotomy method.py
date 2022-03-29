class Dichotomy:
    def __init__(self, func, left, right, e):
        self._func = func
        self._e = e
        self._l = left
        self._r = right

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
        return left + right / 2, i, right - left

    def do(self):
        return Dichotomy.do_method(self._func, self._l, self._r, self._e)

