import math
import random

inSquare = 0
inCircle = 0
for i in range(1000000):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    inSquare += 1
    if math.sqrt((x ** 2) + (y ** 2)) <= 1:
        inCircle += 1

piApprox = (inCircle / inSquare) * 4
print(piApprox)