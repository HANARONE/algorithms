from itertools import permutations

def solution(k, dungeons):
    per = permutations(dungeons, len(dungeons))
    max_cnt = 0
    
    for e in per:
        life = k
        cnt = 0        
        for i in range(len(dungeons)):
            if life >= e[i][0]:
                life -= e[i][1]
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                break
    
    return max_cnt