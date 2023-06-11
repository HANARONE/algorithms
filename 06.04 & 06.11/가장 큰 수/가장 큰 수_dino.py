def solution(numbers):
    numbers = list(map(str, numbers))
    # 람다함수로 한 줄로 해봤다
    numbers.sort(key = lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
