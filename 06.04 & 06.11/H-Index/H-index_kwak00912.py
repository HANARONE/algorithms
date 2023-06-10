def solution(citations):
    h_index = 0
    
    n = len(citations) # n = 발표한 논문의 수
    
    for h in range(n+1): # 1) 인용된 논문 0편 부터 n편까지
        cnt = 0 # 카운트로 h번 이상 인용된 논문 세기
        for j in range(n):
            if citations[j] >= h: #0부터 n번 이상 인용된 논문일 때
                cnt += 1 # 카운트 세기
        if cnt >= h: # h번 이상 인용된 논문이 h편 이상이면
            h_index = h # h_index = h 로 판단함. 반복.
    
    return h_index  