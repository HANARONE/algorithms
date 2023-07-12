def solution(cards1, cards2, goal):
    answer = ''
    leng = len(goal)
    
    for i in range(leng):
        len1 = len(cards1)
        len2 = len(cards2)
        x = goal[i]
        
        if len1 != 0 and cards1[0] == x:
            cards1.pop(0)
            
        elif len2 != 0 and cards2[0] == x:
            cards2.pop(0)
            
        else:
            answer = 'No'
            return answer

    answer = 'Yes'    
    return answer