# class 老师的代码不保熟可还行！？？
print('\nAnimal')
class Ani:


    def __init__(self, name):
        self.name = name

    def walk(self):
        return 'walking'

    def sleep(self):
        return 'sleeping'

    def speak(self):
        return '不知道'


class Dog(Ani):


    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        return super().speak() # 调用上级

    def nianl(self):
        return self.age


my_dog = Dog("X", "2")
print(my_dog.talk())


class Animal(object):
   def __init__(self, name, age):
       self.name = name
       self.age = age

   def call(self):
       print(self.name, '会叫')

class Cat(Animal):
   def __init__(self,name,age,sex):
       super(Cat, self).__init__(name,age)  # 不要忘记从Animal类引入属性
       self.sex=sex

if __name__ == '__main__':  # 单模块被引用时下面代码不会受影响，用于调试
   c = Cat('喵喵', 2, '男')  #  Cat继承了父类Animal的属性
   c.call()



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
