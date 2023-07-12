def solution(n, m, section):
    answer = 0
    max_r = 100000
    paint = [0] * (n+1)
    
    for x in section:
        paint[x] = 1
    
    cnt = 0
    for i in range(n+1):
        if paint[i] == 1:
            for j in range(m):
                if i + j <= n:
                    paint[i+j] = 0
            
            cnt += 1

    return cnt