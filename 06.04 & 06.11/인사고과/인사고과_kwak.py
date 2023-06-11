def solution(scores):
    result = 0
    lens = len(scores)
    
    for i in range(lens):
        cnt = 0
        for j in range(lens):
            if scores[i][0] < scores[j][0] and scores[i][1] < scores[j][1]:
                cnt += 1
        if cnt >= 1:
            scores[i] = [-1, -1]

    rank = 1
    s_scores = [0] * lens
    
    for k in range(lens):
        s_scores[k] = scores[k][0] + scores[k][1]

    for l in range(lens):
        if s_scores[0] < s_scores[l]:
            rank += 1

        if s_scores[0] == -2:
            result = -1
        else:
            result = rank

    return result