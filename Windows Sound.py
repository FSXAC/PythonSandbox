import time

time_left = 3

def timeisup():
    for i in range(5):
        print("\a")

def timealarm():
    print("\a")
    print("\a")
    time.sleep(1)

while True:
    time.sleep(1)
    print("\a", time_left)

    if time_left <= 0.:
        print("\b Time is up!")
        break
    
    time_left -= 1

input()

for i in range(10):
    timealarm()
    
