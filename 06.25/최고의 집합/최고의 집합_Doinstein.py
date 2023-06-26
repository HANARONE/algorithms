def solution(n, s):
    if n>s:
        return [-1]
    else:
        answer = [s//n]*n
        for i in range(s%n):
            answer[i] += 1
        return sorted(answer)