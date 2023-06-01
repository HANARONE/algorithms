def solution(answers):
    n = len(answers)
    
    # 수포자 찍는 방식
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]
    
    # 수포자 점수 초기화
    score = [0,0,0]  
    
    # 수포자 정답 체크
    for i in range(n):
        if answers[i] == a1[i%len(a1)]: # 찍는 방식 돌리기
            score[0]+=1
        if answers[i] == a2[i%len(a2)]:
            score[1]+=1
        if answers[i] == a3[i%len(a3)]:
            score[2]+=1
    
    # 가장 많은 문제를 맞힌 사람 리스트 초기화
    ans = []
    
    # 최고점 사람 체크
    for i in range(len(score)):
        if score[i] == max(score):  
           ans.append(i+1) # 최고점과 동일한 사람 인덱스 + 1
    return sorted(ans)