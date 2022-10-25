
def is_leap(year):
    leap = False
    if (year%4==0 and year%100!=0) or (year%400 == 0):
        leap = True
        print(f"{year} is leap year")
    else:
        leap = False
        print(f"{year} is not leap year")    
    return leap


year = int(input())
print(is_leap(year))
