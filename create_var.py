import os
import random

path = "variant" + (input("Enter variant number (default random 1-10): ") or str(random.randint(1, 10)))
os.mkdir(path)
t = int(input('Enter tasks count (default 4): ') or "4")
for i in range(1, t+1):
    open(os.path.join(path, 'task' + str(i) + '.py'), 'w').close()
