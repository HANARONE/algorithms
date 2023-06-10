def solution(array, commands):
    answer = []
        
    for i in commands:
        a = i[0]
        b = i[1]
        c = i[2]
        # commands 안에 있는 리스트의 값 입력
        ar = sorted(array[a-1:b])
        # 슬라이싱하고 배열
        answer.append(ar[c-1])
        # 목표값 입력
    
    return answer