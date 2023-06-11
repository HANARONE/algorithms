
# 순열 가져오고
from itertools import permutations


def solution(k, dungeons):
    # return answer 변수 초기화
    answer = 0
    # 순열로 모든 case를 cases 배열로 저장한다
    cases = list(permutations(dungeons, len(dungeons)))
    # case 하나씩 완탐 돌리며너 탐험할 수 있는 던전 수 count
    for case in cases:
        temp, cnt = k, 0
        for need, consume in case:
            # 필요한 피로도보다 남아있는 피로도가 많다면 해당 던전에 갈 수 있다.
            if temp >= need:
                temp -= consume
                cnt += 1
                
        answer = max(answer, cnt)
        
    return answer
