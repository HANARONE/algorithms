def solution(k, m, score):
    result = 0
    lens = len(score)
    box = lens // m
    score.sort(reverse = True)
    
    for i in range(box):
        j = (i+1) * m - 1
        result += score[j] * m
        
    return result