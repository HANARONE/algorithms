# 중복 순열로 풀면 풀릴 것이라 생각
# 중복 순열 product
# for e in product([1, 2], repeat = 2):
# [1, 1], [1, 2], [2, 1], [2, 2] 

from itertools import product

def solution(word):
    answer = []
    #repeat = 1 ~ 5 
    for i in range(1, 6):
        # 하나씩 빼기
        for e in product(['A','E','I','O','U'], repeat = i):
            # join해서 글자 형태로 k로 저장
            k = ''.join(e)
            # answer에 하나씩 추가
            answer.append(k)
    
    # 정렬(정렬하면 기본으로 사전식 정렬)
    answer.sort()
    # 인덱스 번호만 뽑으면 되는데, 0번째분터 시작하므로 +1
    result = answer.index(word) + 1
    return result