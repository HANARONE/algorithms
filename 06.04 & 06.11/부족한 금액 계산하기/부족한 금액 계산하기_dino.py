def solution(price, money, count):
    result = 0
    
    # 다 순회해본다. 완전 탐색
    for i in range(count):
        # 남은 돈 세기
        money = money - (price * (i+1))
        
    if money >= 0:
        result = 0
    else:
        # 얼마 모자르는지
        result = -(money)
    
    return result
