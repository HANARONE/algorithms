def solution(sizes):
    answer = 0
    height = []
    width = []
    new_list = []
    
    for i in range(len(sizes)):
        sizes[i] = sorted(sizes[i], reverse=True)
    new_list = sorted(sizes, reverse=True)
    
    for i in range(len(new_list)):
        height.append(sizes[i][0]) 
        width.append(sizes[i][1])

    answer = max(height) * max(width)
    
    return answer