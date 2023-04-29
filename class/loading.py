"""
import time
while True:
    for i in range(10):
        val = "\b\r"+i*" "+"=="
        print(val,end = "=")
        time.sleep(1)
    print("\b", end = "")

print()
"""

import time
import sys

#animation = "|/-\\"

#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]

animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
i = 0

while True:
    time.sleep(0.1)
    sys.stdout.write("\rwaiting.... " + animation[i % len(animation)])
    sys.stdout.flush()
    i += 1


