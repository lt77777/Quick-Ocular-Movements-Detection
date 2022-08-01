import sys
import time
sys.path.insert(0, "./main")
from webcam_measurement import *

# 3 second delay
time.sleep(3)
# Before measurement
webcam_measurement(3)
# Cover
time.sleep(1)
# After measurement
webcam_measurement(3)