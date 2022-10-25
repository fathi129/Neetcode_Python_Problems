
import math
import os
import random
import re
import sys
from datetime import datetime as dt
# Complete the time_delta function below.
def time_delta(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'
    t1tm = dt.strptime(t1,fmt)
    t2tm = dt.strptime(t2,fmt)
    delta =str(round(abs((t1tm-t2tm).total_seconds())))
    return delta
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        print(delta)
    #     fptr.write(str(delta) + '\n')       
    # fptr.close()
