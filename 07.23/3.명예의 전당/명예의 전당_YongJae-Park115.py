def solution(k, score):
    answer = []
    a = []
    for i in score:
        if len(a) < k:
            a.append(i)
        else:
            if i > min(a):
                a.remove(min(a))
                a.append(i)
        answer.append(min(a))
    return answer