
def print_inverted_half_pyramid(N):
    for i in range(N):
        for j in range(N-i):
            print("*", end=" ")
        print()

print_inverted_half_pyramid(5)