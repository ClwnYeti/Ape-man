class Parabolic:
    def __init__(self, func):
        self._func = func

    @staticmethod
    def do_method(func, left, right, e):
        i = 0
        middle = (left + right) / 2
        fl = func(left)
        fm = func(middle)
        fr = func(right)
        while (fm < fl and fm < fr) or right - left > e:
            i += 1
            u = middle -\
                ((middle - left)**2 * (fm - fr) - (middle - right)**2 * (fm - fl)) /\
                (2 * abs((middle - left) * (fm - fr) - (middle - right) * (fm - fl)))
            fu = func(u)
            if fu <= fm:
                if u < middle:
                    right = middle
                else:
                    left = middle
                    middle = u
            else:
                if u < middle:
                    left = u
                else:
                    right = u
        return u, i, right - left

    def do(self, left, right, e):
        return Parabolic.do_method(self._func, left, right, e)
