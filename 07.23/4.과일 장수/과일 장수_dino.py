def solution(k, m, score):
    answer = 0
    # 그룹별로 가장 낮은 점수인 사과가 나중에 버려져야 최적이니까 일단 내림차순 sort
    score = sorted(score, reverse=True)

    # (사과 인덱스번호 + 1)이 m의 배수일 때, 최하점수이므로 그게 곧 가격
    for i, v in enumerate(score):
        if (i + 1) % m == 0:
            answer += v * m

    return answer