def solution(scores):
    answer = 1
    me = scores[0]
    me_score = sum(me)
    scores.sort(key=lambda x: (-x[0], x[1]))
    check = 0

    for score in scores:
        if me_score >= sum(score):
            continue

        if me[0] < score[0] and me[1] < score[1]:
            return -1

        if check <= score[1]:
            check = score[1]
            answer += 1

    return answer
