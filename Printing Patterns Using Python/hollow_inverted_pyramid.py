def print_hollow_inverted_pyramid(N):
    for i in range(N):
        for j in range(N-i):
            if j == 0 or j==N-i-1 or i==0 or i==N-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
print_hollow_inverted_pyramid(7)