def rotate(arr,x1,y1,x2,y2):
    num_lst = [arr[x1 - 1][y1 - 1]] # 시작값
    for i in range(y1, y2): # 위쪽
        num_lst.append(arr[x1 - 1][i]) 
        arr[x1 - 1][i] = num_lst[-2] # append 이전 마지막 값으로 arr 변경
    for i in range(x1, x2): # 오른쪽
        num_lst.append(arr[i][y2 - 1])
        arr[i][y2 - 1] = num_lst[-2]
    for i in range(y2 - 2, y1 - 2, -1): # 아래쪽
        num_lst.append(arr[x2 - 1][i])
        arr[x2 - 1][i] = num_lst[-2]
    for i in range(x2 - 2, x1 - 2, -1): # 왼쪽 
        num_lst.append(arr[i][y1 - 1])
        arr[i][y1 - 1] = num_lst[-2]
    return arr, min(num_lst)

def solution(rows, columns, queries):
    matrix = [[i+(j)*columns for i in range(1,columns+1)] for j in range(rows)]
    ans = []
    for x1,y1,x2,y2 in queries:
        matrix,tmp = rotate(matrix,x1,y1,x2,y2)
        ans.append(tmp)
        
    return ans