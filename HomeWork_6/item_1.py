# Класс Светофор
from itertools import cycle
from time import sleep
import datetime

class TrafficLight:
    __colors = {'red': 7, 'yellow': 2, 'green': 9}

    def __init__(self, count_cycle):
       self.count_cycle = count_cycle

    def running(self):
        iter_sec = 1
        for color, sec in cycle(TrafficLight.__colors.items()):
            if iter_sec > self.count_cycle * 3:
                break
            print(color)
            print(datetime.datetime.now().strftime('%H:%M:%S'))
            sleep(sec)
            iter_sec+=1

trafficlight_001 = TrafficLight(1)
trafficlight_001.running()
print(datetime.datetime.now().strftime('%H:%M:%S'))
