def solution(k, score):
    answer = []
    a = []

    for i in score:
        # 아직 명예의 전당에 오를 자리가 남아있으면 추가
        if len(a) < k:
            a.append(i)
        # 최하위권자랑 비교
        # 자리가 다 꽉 찼다면, 최하위 순위권자랑 비교해서 더 낮은 놈 제거해주고 새로 추가해준다
        else:
            if min(a) < i:
                a.remove(min(a))
                a.append(i)

        answer.append(min(a))

    return answer