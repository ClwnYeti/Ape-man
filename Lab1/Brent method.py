import math


class Brent:
    def __init__(self, func, a, b, e, max_iter):
        self._func = func
        self._a = a
        self._b = b
        self._e = e
        self._max_iter = max_iter

    @staticmethod
    def top_of_parabola(func, x, w, v):
        fx = func(x)
        fw = func(w)
        fv = func(v)
        denominator = 2 * ((w - x) * (fw - fv) - (w - v) * (fw - fx))
        if denominator == 0:
            return None
        return w - ((fw - fv) * (w - x) ** 2 - (fw - fx) * (w - v) ** 2) / denominator

    @staticmethod
    def do_method(func, a, b, e, max_iter):
        r = (3 - 5 ** 0.5) / 2
        x = w = v = a + r * (b - a)
        d_cur = d_prv = b - a
        i = 0
        while i < max_iter:
            i += 1
            if max(x - a, b - x) < e:
                break
            g = d_prv / 2
            d_prv = d_cur
            u = Brent.top_of_parabola(func, x, w, v)
            if u is None or abs(u - x) > g or u < a or u > b:
                if x < (a + b) / 2:
                    u = x + r * (b + x)
                    d_prv = b - x
                else:
                    u = x - r * (x - a)
                    d_prv = x - a
            d_cur = abs(u - x)
            if func(u) > func(x):
                if u < x:
                    a = u
                else:
                    b = u
                if func(u) <= func(w) or w == x:
                    v = w
                    w = u
                else:
                    if func(u) <= func(w) or v == x or v == w:
                        v = u
            else:
                if u < x:
                    b = x
                else:
                    a = x
                v = w, w = x, x = u
        return x

    def do(self):
        return Brent.do_method(self._func, self._a, self._b, self._e, self._max_iter)


f = lambda x: x ** 2 + 3 * x - 4
brent = Brent(f, 2, 5, 10e-5, 50)
print(brent.do())
