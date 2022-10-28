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