def solution(t, p):
    answer = 0
    lent = len(t)
    lenp = len(p)
    tlist = list(map(str, t))
    
    cnt = 0
    for i in range(lent - lenp + 1):
        x = int(''.join(tlist[i:i+lenp]))
        if int(p) >= x:
            cnt += 1
  
    return cnt