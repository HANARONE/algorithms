def solution(k, score):
    answer = []
    tmp=[]
    for s in score:
        tmp.append(s)
        tmp.sort(reverse=True)
        if len(tmp)>k:
            tmp.pop()
        answer.append(tmp[-1])
    
    return answer