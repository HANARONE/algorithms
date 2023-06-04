def solution(sizes):
    answer = 0
    sizes = list(map(lambda x: sorted(x),sizes)) # 명함의 짧은 부분이 왼쪽/ 긴 부분이 오른쪽
    mx,my = -1e9,-1e9 # 최대값 구하기 위해 초기화
    for x,y in sizes:
        mx = max(mx,x) # 짧은 부분 중 가장 긴 길이
        my = max(my,y) # 긴 부분 중 가장 긴 길이
        
    return mx*my