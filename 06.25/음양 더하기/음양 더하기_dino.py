# 메모이제이션 기법 사용하기 위해 memo라는 딕셔너리 초기화
memo = {}


# 함수로 정의하여 풀이
# num : 테이블에 앉은 사람 , left : 테이블에 아직 앉지 못 한 사람
def solution(left, num):
    #
    key = str([left, num])
    # 종료 조건
    if key in memo:
        return memo[key]
    if left < 0:
        return 0
    if left == 0:
        return 1

    # 재귀 처리
    count = 0
    cnt = 0
    for i in range(num, 6 + 1):
        print("i 는", i, "count는", count, ",,,, 연산은", cnt, "번 째 하는 중")
        count += solution(left - i, i)
        cnt += 1
        # print("i 는", i, "count는", count, ",,,, 연산은", cnt, "번 째 하는 중")
    # 메모화 처리
    memo[key] = count
    print("---------------")
    print("key", key, "count", count)
    # 종료
    return count


print(solution(6, 2))