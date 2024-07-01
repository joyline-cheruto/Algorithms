def tower_of_hanoi(n, A, B, C):
    if n == 1:
        print(" move disk from ",A,"to",C)
        return 1
