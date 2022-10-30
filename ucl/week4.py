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


# class 老师的代码不保熟可还行！？？
print('\nAnimal')




# 红绿灯
class TrafficLight:

    def __init__(self):
        self.__green = False
        self.__orange = False
        self.__red = False
        self.is_upward = False

    def next_state(self):
        if self.__green:
            self.__green = False
            self.__orange = True
        elif self.__orange:
            self.__orange = False
            if not self.is_upward:
                self.__red = True
                self.is_upward = True
            else:
                self.__green = True
                self.is_upward = False
        elif self.__red:
            self.__red = False
            self.__orange = True
        else:
            self.__green = True

    def get_state(self):
        res = ''
        if self.__green:
            res = res + '\033[1m\033[92mO\033[0m'
        else:
            res = res + 'O'
        if self.__orange:
            res = res + '\033[1m\033[93mO\033[0m'
        else:
            res = res + 'O'
        if self.__red:
            res = res + '\033[1m\033[91mO\033[0m'
        else:
            res = res + 'O'
        return res

        def set_green(self, state):
            self.__green = state

        def set_orange(self, state):
            self.__orange = state

        def set_red(self, state):
            self.__red = state


class ResettableTrafficLight(TrafficLight):

    def reset(self):
        self.set_green(False)
        self.set_orange(False)
        self.set_red(False)
        self.is_upward = False


traffic_light = TrafficLight()

print("The light state is", traffic_light.get_state())
for _ in range(10):
    traffic_light.next_state()
    print("The light state is", traffic_light.get_state())
