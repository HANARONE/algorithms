def solution(name, yearning, photo):
    answer = []
    # 딕셔너리 생성
    # zip으로 묶어주고
    # dict로 딕셔너리 형태 변환
    # ex) {'may': 5, 'kein': 10, 'kain': 1, 'radi': 3}
    dic = dict(zip(name, yearning))
        
    for row in photo:
        sum_val = 0
        for elem in row:
            if elem in dic: # elem이 dic에 있으면
                sum_val += dic[elem] # dic[elem] 값 sum 추가
        
        answer.append(sum_val)
    
    
    return answer