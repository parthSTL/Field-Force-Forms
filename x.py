import sys, os
import time

counter = 0
while (True):
    os.system("python "+ "load_data.cpython-39.pyc")
    counter+=1
    print(counter)
    time.sleep(1)

