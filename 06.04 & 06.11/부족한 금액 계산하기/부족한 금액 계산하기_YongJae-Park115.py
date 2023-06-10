def solution(price, money, count):
    a=[]    
    # 순차적으로 늘어나는 가격 들어갈 리스트
    for i in range(1,count+1):
        a.append(i*price)
        # n번 탈때마다 가격에 n곱하고 a리스트에 추가
    price = sum(a)
    # 가격의 총합
    if money >= price:
        return 0
        # 가지고 있는 돈이 총가격보다 많을 경우
    else:
        return price - money
    # 가지고 있는 돈이 총가격보다 적을 경우
    
    
def solution(price, money, count):
    sum_val = 0
# 처음에 이렇게 풀었는데 sum_val = 0 설정안하고
    for i in range(1,count+1):
        sum_val += i*price
# 여기서 price += i*price 로 풀면서 틀림. 뭐가 잘못된지도 몰라서 위에 방식으로 품
# 분발 요망
    if sum_val >= money:
        return sum_val-money
    else:
        return 0