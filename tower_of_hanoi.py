def tower_of_hanoi(n, A, B, C):
    if n == 1:
        print(" move disk from ",A,"to",C)
        return 1
    else:
        tower_of_hanoi(n-1,A,C,B)
        move (A,C)
        tower_of_hanoi(n-1,B,A,C)