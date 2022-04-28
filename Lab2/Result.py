import numpy as np
from matplotlib import pyplot as plt
from GradientDescent import GradientDescent
from StepConst import StepConst
from StepSplit import StepSplit
from StepFibonacci import StepFibonacci
from StepGoldenRatio import StepGoldenRatio


def draw(a, b, func, points_x, points_y, name):
  fig, ax = plt.subplots()
  x, y = np.mgrid[a:b:100j, a:b:100j]
  ax.set_title(name)
  ax.contour(x, y, func([x, y]), levels=50, colors='#ccffff')
  for i in range(len(points_x)):
    ax.scatter(points_x[i], points_y[i], c='#ff0004')
  ax.plot([points_x[i] for i in range(len(points_x))], [points_y[i] for i in range(len(points_y))], c='#ff0004')
  plt.savefig(name + ".png")
  plt.show()


def func1(point):
    return point[0] ** 2 + 7 * point[1] ** 2 + point[0] * point[1] + 1


def func2(point):
    return (point[0] + 2 * point[1] - 7) ** 2 + (2 * point[0] + point[1] - 5) ** 2


start_point = [1., 1.]
eps = 1e-7
# fig = plt.figure()
# a = fig.add_axes([0, 0, 1, 1], projection='3d')
func1_StepConst = GradientDescent.do_descent(func1, StepConst(10), eps, start_point)
print(f"Name: func1_StepConst, Count of Steps: {func1_StepConst[0]}, Minimal_point: {func1_StepConst[1]}")
draw(-2, 2, func1, [i[0] for i in func1_StepConst[2]], [i[1] for i in func1_StepConst[2]], "func1_StepConst")
# a.set_title("func1_StepConst")
# a.plot([i[0] for i in func1_StepConst[2]],
#        [i[1] for i in func1_StepConst[2]],
#        [func1(i) for i in func1_StepConst[2]])
# plt.savefig("func1_StepConst.png")
# a.clear()

func1_StepSplit = GradientDescent.do_descent(func1, StepSplit(10, 0.5), eps, start_point)
print(f"Name: func1_StepSplit, Count of Steps: {func1_StepSplit[0]}, Minimal_point: {func1_StepSplit[1]}")
draw(-2, 2, func1, [i[0] for i in func1_StepSplit[2]], [i[1] for i in func1_StepSplit[2]], "func1_StepSplit")
# a.set_title("func1_StepSplit")
# a.plot([i[0] for i in func1_StepSplit[2]],
#        [i[1] for i in func1_StepSplit[2]],
#        [func1(i) for i in func1_StepSplit[2]])
# plt.savefig("func1_StepSplit.png")
# a.clear()

func1_StepFibonacci = GradientDescent.do_descent(func1, StepFibonacci(10), eps, start_point)
print(f"Name: func1_StepFibonacci, Count of Steps: {func1_StepFibonacci[0]}, Minimal_point: {func1_StepFibonacci[1]}")
draw(-2, 2, func1, [i[0] for i in func1_StepFibonacci[2]], [i[1] for i in func1_StepFibonacci[2]], "func1_StepFibonacci")
# a.set_title("func1_StepFibonacci")
# a.plot([i[0] for i in func1_StepFibonacci[2]],
#        [i[1] for i in func1_StepFibonacci[2]],
#        [func1(i) for i in func1_StepFibonacci[2]])
# plt.savefig("func1_StepFibonacci.png")
# a.clear()

func1_StepGoldenRatio = GradientDescent.do_descent(func1, StepGoldenRatio(10), eps, start_point)
print(f"Name: func1_StepGoldenRatio, Count of Steps: {func1_StepGoldenRatio[0]}, Minimal_point: {func1_StepGoldenRatio[1]}")
draw(-2, 2, func1, [i[0] for i in func1_StepGoldenRatio[2]], [i[1] for i in func1_StepGoldenRatio[2]], "func1_StepGoldenRatio")
# a.set_title("func1_StepGoldenRatio")
# a.plot([i[0] for i in func1_StepGoldenRatio[2]],
#        [i[1] for i in func1_StepGoldenRatio[2]],
#        [func1(i) for i in func1_StepGoldenRatio[2]])
# plt.savefig("func1_StepGoldenRatio.png")
# a.clear()

func2_StepConst = GradientDescent.do_descent(func2, StepConst(10), eps, start_point)
print(f"Name: func2_StepConst, Count of Steps: {func2_StepConst[0]}, Minimal_point: {func2_StepConst[1]}")
draw(-1, 5, func1, [i[0] for i in func2_StepConst[2]], [i[1] for i in func2_StepConst[2]], "func2_StepConst")
# a.set_title("func2_StepConst")
# a.plot([i[0] for i in func2_StepConst[2]],
#        [i[1] for i in func2_StepConst[2]],
#        [func1(i) for i in func2_StepConst[2]])
# plt.savefig("func2_StepConst.png")
# a.clear()

func2_StepSplit = GradientDescent.do_descent(func2, StepSplit(10, 0.5), eps, start_point)
print(f"Name: func2_StepSplit, Count of Steps: {func2_StepSplit[0]}, Minimal_point: {func2_StepSplit[1]}")
draw(-1, 5, func1, [i[0] for i in func2_StepSplit[2]], [i[1] for i in func2_StepSplit[2]], "func2_StepSplit")
# a.set_title("func2_StepSplit")
# a.plot([i[0] for i in func2_StepSplit[2]],
#        [i[1] for i in func2_StepSplit[2]],
#        [func1(i) for i in func2_StepSplit[2]])
# plt.savefig("func2_StepSplit.png")
# a.clear()

func2_StepFibonacci = GradientDescent.do_descent(func2, StepFibonacci(10), eps, start_point)
print(f"Name: func2_StepFibonacci, Count of Steps: {func2_StepFibonacci[0]}, Minimal_point: {func2_StepFibonacci[1]}")
draw(-1, 5, func1, [i[0] for i in func2_StepFibonacci[2]], [i[1] for i in func2_StepFibonacci[2]], "func2_StepFibonacci")
# a.set_title("func2_StepFibonacci")
# a.plot([i[0] for i in func2_StepFibonacci[2]],
#        [i[1] for i in func2_StepFibonacci[2]],
#        [func1(i) for i in func2_StepFibonacci[2]])
# plt.savefig("func2_StepFibonacci.png")
# a.clear()

func2_StepGoldenRatio = GradientDescent.do_descent(func2, StepGoldenRatio(10), eps, start_point)
print(f"Name: func2_StepGoldenRatio, Count of Steps: {func2_StepGoldenRatio[0]}, Minimal_point: {func2_StepGoldenRatio[1]}")
draw(-1, 5, func1, [i[0] for i in func2_StepGoldenRatio[2]], [i[1] for i in func2_StepGoldenRatio[2]], "func2_StepGoldenRatio")
# a.set_title("func2_StepGoldenRatio")
# a.plot([i[0] for i in func2_StepGoldenRatio[2]],
#        [i[1] for i in func2_StepGoldenRatio[2]],
#        [func1(i) for i in func2_StepGoldenRatio[2]])
# plt.savefig("func2_StepGoldenRatio.png")
# a.clear()
