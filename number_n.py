if __name__ == "__main__":
    n = int(input())
    # for i in range(1,n+1):
    #     for j in range(1,i+1):
    #         print(j,end=" ")
    #     print()
    sum = 1
    for i in range(2,n+1):
        sum = sum*10 + i 
    print(sum,end="")   

