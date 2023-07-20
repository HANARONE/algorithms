def solution(s):
    result = []
    answer = {}
    lens = len(s)
    
    for i in range(lens):
        x = s[i]
        if x in answer:
            result.append(i - answer[x])
            answer[x] = i
            
        else:
            result.append(-1)
            answer[x] = i
            
    return result