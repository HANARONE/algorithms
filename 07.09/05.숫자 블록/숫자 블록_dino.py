'''sketch
0부터 len(블록)까지 각 수의 배수(2배수부터 체크),
가장 큰 수의 배수가 마지막으로 체크.
만약 소수라면 1이 저장
소수가 아니라면 각 숫자의 약수 중 본인을 제외한 가장 큰 약수가 마지막으로 저장된다

범위가 백만이니까 시간 초과임
'''


def prime_num(x):
    for i in range(2, x):
        if x % i == 0:
            return False
            break
    return True


def solution(begin, end):
    answer = []
    for num in range(begin, end + 1):
        if num == 1:
            answer.append(0)
            continue
        else:
            if prime_num(num):
                answer.append(1)
            else:
                for i in range(num - 1, 1, -1):
                    if num % i == 0:
                        answer.append(i)
                        break

    return answer



'''
2번째 풀이
'''


def solution(begin, end):
    answer = []

    for num in range(begin, end + 1):
        if num == 1:
            answer.append(0)
        else:
            x = 1

            for i in range(2, int(num ** (1 / 2)) + 1):
                if num % i == 0:
                    x = i
                    if num // i <= 10000000:
                        x = num // i
                        break
            answer.append(x)
    return answer