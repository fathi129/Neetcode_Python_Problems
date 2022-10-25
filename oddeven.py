import math
import os
import random
import re
import sys

if __name__ == "__main__":
    n = int(input().strip())
    print(n)
    if(n%2 == 0):
        if(n>=2) & (n<5):
            print(f"{n} is even..range between 2 and 5 it is not weird")
        elif(n>=6) & (n<=20):
            print(f"{n} is even..range between 6 and 20 and it is weird")
        elif(n>20):
            print(f"{n} is even..greater than 20 it is not weird")
    else:
        print(f"{n} is odd...weird")    
