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
