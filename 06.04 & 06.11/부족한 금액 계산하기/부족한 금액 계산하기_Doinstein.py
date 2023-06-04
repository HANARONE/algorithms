def solution(price, money, count):
    ps = 0
    
    # 총 금액 계산
    for i in range(1,count+1):
        ps+= price*i
    
    # 현재 금액과 총 금액 비교
    if ps >= money:
        return ps-money
    else:
        return 0
        