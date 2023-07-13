def solution(t, p):
    n = len(p)
    cnt = 0
    for i in range(len(t)-n+1):
        if int(t[i:i+n])<=int(p):
            cnt+=1
            
    return cnt