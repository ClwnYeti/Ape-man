import numpy as np
from scipy import optimize


machineAcc = 0.000000001

# Метод сопряженных градиентов (Флетчера-Ривса)
# Градиентный поиск минимума

Path = []


def fr(x0, h, e, f):
    x_cur = np.array(x0)
    Path.append(x_cur)
    h = np.array(h)
    n = len(x0)
    k = 0  # step1
    grad = optimize.approx_fprime(x_cur, f, e ** 4)  # step2
    prev_grad = 1
    pk = -1 * grad
    while any([abs(grad[i]) > e ** 2 for i in range(n)]):  # step3
        if k % n == 0:  # step4
            pk = -1 * grad
        else:
            bk = (np.linalg.norm(grad) ** 2) / (np.linalg.norm(prev_grad) ** 2)  # step5
            prev_pk = pk
            pk = -1 * grad + bk * prev_pk  # step6
        a = optimize.minimize_scalar(lambda x: f(x_cur + pk * x), bounds=(0,)).x
        x_cur = x_cur + a * pk  # step8
        Path.append(x_cur)
        k = k + 1  # step8
        prev_grad = grad
        grad = optimize.approx_fprime(x_cur, f, e ** 4)  # step2
    return x_cur  # step10
