 import numpy as np
import matplotlib.pyplot as plt

"""
My take on this challenge:

There are 100 doors in a row that are all initially closed.
You make 100 passes by the doors.
The first time through, visit every door and  toggle  the door  (if the door is closed,  open it;   if it is open,  close it).
The second time, only visit every 2nd door   (door #2, #4, #6, ...),   and toggle it.
The third time, visit every 3rd door   (door #3, #6, #9, ...), etc,   until you only visit the 100th door.


Task:
What state are the doors in after the last pass?   Which are open, which are closed? 
"""

doors = [0]*100
visits = [0]*100

for p in range(100):
    for d in range(p, 100, p+1):
        doors[d] = int(not doors[d])
        visits[d] += 1

print(doors)

# Bar plot of time each door was visited
print(visits)
plt.figure(figsize=(30, 10))
plt.bar(range(100), visits, width=0.4)
plt.xticks(np.arange(0, 100, 1))
plt.yticks(np.arange(0, max(visits)+1, 1))
plt.xlabel("Door Number")
plt.ylabel("Times Flipped")
plt.xticks(rotation=90)
plt.grid(False)
plt.show()
