import time
while True:
    print("Loading",end = "")
    for i in range(10):
        print(".",end = '',flush=True)
        time.sleep(0.5)
        if i == 9:
            print("\r",end='')
