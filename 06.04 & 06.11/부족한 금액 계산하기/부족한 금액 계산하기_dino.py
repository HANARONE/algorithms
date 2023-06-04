def solution(price, money, count):
    result = 0

    for i in range(count):
        money = money - (price * (i+1))

    if money >= 0:
        result = 0
    else:
        result = -(money)

    return result
