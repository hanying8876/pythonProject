# matplotlib notebook 画图小典籍
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [0, 0, 1, 1])
plt.show()
plt.plot([1, 1, 2, 2, 1], [0, 1, 1, 0, 0])
plt.show()
# 平衡x,y轴用axis('equal'),让坐标系变成正方形
plt.plot([1, 1, 2, 2, 1], [0, 1, 1, 0, 0])
plt.axis('equal')
plt.show()
# 要记得写show()，不写就没有，呵呵
# fill用于填色
plt.fill([1, 1, 2, 2, 1], [0, 1, 1, 0, 0])
plt.axis('equal')
plt.show()
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.show()
# 红色：ro
# 绿色：g
plt.fill([1, 1, 2, 2, 1], [0, 1, 1, 0, 0], 'g')
plt.plot(1.5, 0.5, 'ro')
plt.axis('equal')
plt.show()

# 添加标签，注意要文本引号
plt.fill([1, 1, 2, 2, 1], [0, 1, 1, 0, 0], label='square')
plt.plot(1.5, 0.5, 'ro', label='point')
plt.axis('equal')
plt.legend()
plt.show()

# 来个大的
from collections import OrderedDict

class Plotter:

    def __init__(self):
        plt.figure()

    def add_polygon(self, xs, ys):
        plt.fill(xs, ys, 'lightgray', label='Polygon')

    def add_point(self, x, y, kind=None):
        if kind == 'outside':
            plt.plot(x, y, 'ro', label='Outside')
        elif kind == 'boundary':
            plt.plot(x, y, 'bo', label='Boundary')
            # 蓝色：bo
        elif kind == 'inside':
            plt.plot(x, y, 'go', label='Inside')
            # 绿色：go
        else:
            plt.plot(x, y, 'ko', label='Unclassified')
            # 黑色：ko

    def show(self):
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = OrderedDict(zip(labels, handles))
        plt.legend(by_label.values(), by_label.keys())
        plt.show()

plotter = Plotter()
plotter.add_polygon([1, 1, 2, 2, 1], [0, 1, 1, 0, 0])
# 调用类添加矩形
plotter.add_point(1.5, 0.5)
# 同样方法添加点
plotter.add_point(1.5, 0.5, 'inside')
plotter.add_point(1.5, 0.9, 'Unclassified')
plotter.add_point(1, 1, 'outside')
plotter.add_point(1.5, 1, 'boundary')
plotter.show()

# 哈哈哈哈哈哈

