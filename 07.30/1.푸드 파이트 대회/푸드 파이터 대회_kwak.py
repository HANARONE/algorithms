def solution(food):
    answer = []
    lenf = len(food)
    
    for i in range(1, lenf):
        x = food[i] // 2
        
        for j in range(x):
            answer.append(str(i))
    
    answer.append('0')
    
    for i in range(lenf-1, 0, -1):
        x = food[i] // 2
        
        for j in range(x):
            answer.append(str(i))
            
    answer = ''.join(answer)
    
    return answer