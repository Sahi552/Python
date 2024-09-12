from threading import *
from time import sleep

class one(Thread):
    def run(self):
        for i in range(10):
            print("hello")
            sleep(1)
class two(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)
            
o1 = one()    
o2 = two()

o1.start()
o2.start()

o1.join()
o2.join()

print("end")