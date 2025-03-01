def print_pyramid(N):
    for i in range(N+1):
        for j in range(N-i):
            print(" ",end=" ")
        for k in range(i+1):
            print("*",end=" ")
        for k in range(i):
            print("*",end=" ")
        
        print()
        
print_pyramid(5)
