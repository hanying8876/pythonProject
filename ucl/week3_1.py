# 作业课前没有做，课后火葬场
# 练习5

print('Describe My Sequence (0.1)')  # 依旧是小数点位数，老师好喜欢后一位啊
n = int(input('How many values? '))  # 询问变量
l = []  # 创建list，包含顺序

for i in range(n):
    v = float(input('Insert number ' + str(i + 1) + ': '))
    l.append(v)  # append函数，用于将对象加到函数末尾，append(对象)
print('The statistics are:')
print('* Min:', min(l))  # for循环，list
print('* Max:', max(l))  # for循环，原理同上


# print('* Avg:', average(l)) # for循环，除数直接就是len(l)
# print('* Dup:', dup(l))  # 重复，元组，通过in检查字节是否在元组里，如果in成立则return
# print('* Mod:', mode(l))  #


# 写一堆要写的定义函数

def min(vs):
    res = vs[0]
    for v in vs[1:]:
        if v < res:
            res = v
        return res


def max(vs):
    res = vs[0]
    for v in vs[1:]:
        if v > res:
            res = v
        return res

