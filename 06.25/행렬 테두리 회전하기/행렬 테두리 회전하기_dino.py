'''
f(0) = 0
f(1) = 1
f(2) = 1
f(3) = 1
f(4) = 2
f(5) = 2
f(6) = 4
'''

# 앉힐수있는최소사람수 = 2
# 앉힐수있는최대사람수 = 10
# 전체사람의수 = 100
memo = {}

def solution(left, num) :
    key = str([left, num])
    # 종료 조건
    if key in memo :
        return memo[key]
    if left < 0 :
        return 0
    if left == 0 :
        return 1

    # 재귀 처리
    count = 0
    for i in range(num, 6 + 1) :
        count += solution(left - i, i)
    # 메모화 처리
    memo[key] = count
    # 종료
    return count

print(solution(6, 2))
