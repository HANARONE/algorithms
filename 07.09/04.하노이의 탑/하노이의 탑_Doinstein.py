def hanoi(A, C, B, n):
    if n == 0:
        return []
    return hanoi(A, B, C, n-1) + [[A, C]] + hanoi(B, C, A, n-1)

def solution(n):
    return hanoi(1, 3, 2, n)