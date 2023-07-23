def solution(number, limit, pow):
    answer = 0
    div = [1]

    for i in range(2, number + 1):
        cnt = 0
        # number가 10만이니까 제곱근까지만 세자
        for j in range(1, int(i ** (1 / 2) + 1)):
            if i % j == 0:
                cnt += 1
                # 제곱근의 제곱은 중복이니까
                if j ** 2 != i:
                    cnt += 1

        # 문제 조건 공격력 제한
        if cnt > limit:
            cnt = pow
            div.append(cnt)
        else:
            div.append(cnt)

    answer = sum(div)

    return answer