def alpha(a, b):
    if a + b <= 122:
        return (a + b)
    else:
        return (a + b - 97) % 26 + 97

def solution(s, skip, index):
    answer = []
    s_, skip_ = list(s), list(skip)
    lens = len(s)
    lenskip = len(skip)
    
    for i in range(lenskip):
        skip_[i] = ord(skip_[i])
    
    for j in range(lens):
        s_[j] = ord(s_[j])
        
    for k in s_:
        p = 0
        
        for l in range(1, index+1):
            if alpha(k, l) in skip_:
                p += 1
        
        answer.append(alpha(k, (index+p)))
        
    for i in range(len(answer)):
        answer[i] = chr(answer[i])
    
    
    answer = ''.join(answer)
    
    return answer