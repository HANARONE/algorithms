def solution(answers):
    answer = []
    
    # 각 사람의 정답 개수 저장(g1 맞춘 갯수, g2 맞춘 갯수, g3 맞춘 갯수)
    count = [0,0,0]
    
    # 찍는 패턴 저장
    g1 = [1, 2, 3, 4, 5]
    g2 = [2, 1, 2, 3, 2, 4, 2, 5]
    g3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        # g1
        if answers[i] == g1[(i%5)]:
            count[0] += 1
        
        # g2
        if answers[i] == g2[(i%8)]:
            count[1] += 1
            
        # g3
        if answers[i] == g3[(i%10)]:
            count[2] += 1
    
    # 가장 많은 문제 맞힌 사람 찾기
    for i in range(3):
        if count[i] == max(count):
            answer.append(i+1)
   
    return answer