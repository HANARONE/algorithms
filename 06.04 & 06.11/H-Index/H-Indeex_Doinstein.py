def solution(citations):
    n = len(citations) # 전체 논문 개수

    for i in range(n,0,-1): # 최댓값을 구하기위해 높은 수부터 반복
        tmp = [x for x in citations if x >= i] # 전체 논문 중 h번 이상 인용된 논문 리스트 
        h = len(tmp) # h번 이상 인용된 논문 개수
        if h >= i: # h번 이상 인용된 논문의 개수가 h이상인 경우
            return i 
    return 0 # 없는 경우 0