import time
import math

seconds = time.time()

sNotation = "{:2e}".format(seconds)

print("Seconds since January 1, 1970: ", f'{seconds:,}'," or " ,sNotation, "in Scientific notation")

To_day = time.localtime()
time_string = time.strftime("%m/%d/%Y\n", To_day)

print(time_string)
