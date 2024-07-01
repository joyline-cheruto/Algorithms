def tower_of_hanoi(n, A, B, C):
    if n == 1:
        print(" move disk from ", A, "to", C)
        return 1
    else:
        tower_of_hanoi(n - 1, A, C, B)
        print("Move disk from", A, "to", C)
        tower_of_hanoi(n - 1, B, A, C)


n = int(input("Enter Number of disks:"))
tower_of_hanoi(n, "A", "B", "C")
