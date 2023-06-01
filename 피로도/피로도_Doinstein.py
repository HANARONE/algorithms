from itertools import permutations
def solution(k, dungeons):
    # 모든 던전을 탐험하는 순열 > 순서에 따라 들어갈 수 있는 던전의 수가 다르기 때문
    p =  [i for i in permutations(dungeons,len(dungeons))]
    cnt = -1 # 최대 탐험 개수를 위해 최소 값으로 초기화
    
    for i in p:
        tk,tc = k,0 # i번 루트 초기 피로도 / i번 루트 탐험 개수 초기화
        
        for j in i: # i번 루트에서 던전 탐험
            if tk >= j[0]: # 탐험 가능 여부 체크
                tk -= j[1] # 피로도 소모
                tc += 1 # i번 루트 탐험 개수 1추가
            else:
                break # 더 이상 탐험 불가일 시 반복문 종료
                
        cnt = max(cnt,tc) # 기존 최대 탐험 개수와 i번 탐험 개수 비교
    return cnt