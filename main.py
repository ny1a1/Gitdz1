import random
import time
for i in range(random.randint(1,15)):
    a = random.randint(1,10)
    if a == 10:
        print("Hello World!")
    elif a == 9:
        print("Hello Jhon!")
    elif a == 8:
        print("Hi James!")
    elif a == 5:
        print("Hello, it's United States of America!")
    elif a == 2:
        print("Hello Git!")
    else:
        print("Bay!")
    time.sleep(1)
print("Text")