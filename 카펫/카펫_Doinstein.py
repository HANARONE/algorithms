def solution(brown, yellow):
    tot = brown+yellow # 전체 칸
    for i in range(3,tot): # 중앙이 존재하려면 최소 3*3
        if tot%i == 0: # 전체 칸이 i로 나누어지는 경우 
            x,y = max(tot//i,i),min(tot//i,i) # 큰 값이 가로
            if (x-2)*(y-2) == yellow: # yellow 개수 비교
                return [x,y]