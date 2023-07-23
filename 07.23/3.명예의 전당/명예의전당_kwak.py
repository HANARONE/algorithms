def solution(k, score):
    result = []
    win = []
    lens = len(score)
    
    for i in range(lens):
        win.append(score[i])
        
        if i < k:
            result.append(min(win))
        else:
            win.sort(reverse = True)
            win = win[:k]
            result.append(win[k-1])
            
    return result