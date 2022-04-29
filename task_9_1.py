import time


class TrafficLights:
    __color = 'red', 'yellow', 'green'

    def running(self):
        print(TrafficLights.__color[0])
        time.sleep(7)
        print(TrafficLights.__color[1])
        time.sleep(2)
        print(TrafficLights.__color[2])
        time.sleep(5)


t_lights_1 = TrafficLights()
t_lights_1.running()
