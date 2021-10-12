import time

i = 1
start = time.process_time()

while i > 0:
    i += 1

    if i == 1000000:
        duration = time.process_time() - start
        print("It took {} micros to complete".format(round(duration * 1000000)))
        break
