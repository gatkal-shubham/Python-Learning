def print_half_pyramid(N):
    for i in range(N):
        for j in range(i+1):
            print("*", end=" ")
        print()
print_half_pyramid(10)