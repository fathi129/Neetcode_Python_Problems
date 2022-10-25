arr = [2,1,5,3]
target = 4
# I would iterate the array to find the target by adding the adjacent numbers
print("Sum of numbers")
for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)):
        print("The initial indexes of i and j are",i,j,"\n")
        sum = arr[i]+arr[j]
        print(f"The sum of the values of {arr[i]} and {arr[j]} is {sum}\n")
        if sum==target:
            print(f"The indexes are {i} and {j} for the target {target}")
            break
    if sum==target:
        break
    



