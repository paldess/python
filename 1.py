
import PyQt5

from time import sleep

class TrafficLight:
    color = 'red'
    def __running(self):
        while True:
            print(f"{TrafficLight.color}")
            sleep(7)
            TrafficLight.color = 'red-yellow'
            print(f"{TrafficLight.color}")
            sleep(2)
            TrafficLight.color = 'green'
            print(f"{TrafficLight.color}")
            sleep(7)
            TrafficLight.color = 'yellow'
            print(f"{TrafficLight.color}")
            sleep(3)


vkl = TrafficLight()
vkl._TrafficLight__running()
