
## 테스트4 실패. 고민
## 단, 금액이 부족하지 않으면 0 을 return 하세요 조건 미확인. 주의!
## 합계를 증가시켜나가서 결국에 가진 money와 비교하여 값을 리턴하는 것을 생각

def solution(price, money, count):
    result = 0
    sum_val = 0
    
    for i in range(count):
        sum_val += price * (i + 1)
        
    if sum_val >= money: # 가지고 있는 금액보다 이용로 합계가 더 많다면,
        result = sum_val - money
    else: # 모자라지 않는다면,
        result = 0
    
    return result

