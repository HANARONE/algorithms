## 1) 처음에 가로 MAX 세로 MAX라고 생각했는데 안됨
## 2) 가로세로가 아니라 긴 축 짧은 축으로 생각하고 풀이하니 수월해졌음.

def solution(sizes):
    result = 0
    long = []
    short = []
    
    # 정렬
    for i in range(len(sizes)):       
        if sizes[i][0] <= sizes[i][1]: # 세로 길이가 더 길면,
            long.append(sizes[i][1]) # 지갑 긴 축에 세로 길이 추가
            short.append(sizes[i][0]) # 지갑 짧은 축에 가로 길이 추가
        else:                         # 가로 길이가 더 길면,
            short.append(sizes[i][1]) # 지갑 짧은 축에 세로 길이 추가
            long.append(sizes[i][0]) # 지갑 긴 축에 가로 길이 추가
# 양 축의 가장 긴 길이 찾기
    long_max = max(long) 
    short_max = max(short)
    
    result = long_max * short_max         
    
    
    return result


