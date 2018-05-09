import os
import time
while True:
    os.system('nvidia-settings -q gpucoretemp | grep gpu:0 >> temp.log');
    print(".")
    time.sleep(5)
    
