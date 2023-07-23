def solution(s):
    result = 0
    lens = len(s)
    arr = ["", 0, 0]
    
    for i in range(lens):
        x = s[i]
        
        if arr[1] == 0:
            arr[0] = x
            arr[1] = 1
            
        elif x == arr[0]:
            arr[1] += 1
        
        elif x != arr[0]:
            arr[2] += 1
            
        if arr[1] == arr[2]:
            result += 1
            arr = ["", 0, 0]
        
        elif i == lens - 1:
            result += 1
            
    return result