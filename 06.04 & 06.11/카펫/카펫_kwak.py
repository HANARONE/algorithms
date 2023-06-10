def solution(brown, yellow):
    result = []
    # 1) 어떻게 계산할까를 우선 생각
    # 2) 노란색 카펫의 가로 길이를 x라고 생각하고 세로 길이를 y 값으로 생각했음. x * y = 카펫 넓이 = 카펫 갯수
    # 3) 위, 아래 양쪽 끝(2개, 2개)을 제거하고 계산 진행
    a = int((brown - 4) / 2)
    
    for y in range(a):
        x = a - y # x + y = a 
        if y * x == yellow and y <= x: # y * x == yellow 값 and 카펫 가로 길이가 세로 길이와 같거나, 세로 길이보다 길다는 조건 추가
            result.append(x+2) # 3)에서 제외한 2개 추가
            result.append(y+2) # 3)에서 제외한 2개 추가
    
    
    return result