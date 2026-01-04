# testing pieces of hardware

import time
from imu import IMU

imu = IMU()
imu.start()

while True:
  print (imu.accel)
  time.sleep(0.1)



