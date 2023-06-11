def solution(answers):
    answer = []
    
    # 각자 찍는 패턴
    pattern_1 = [1,2,3,4,5] # 5 개 단위 패턴 반복
    pattern_2 = [2,1,2,3,2,4,2,5] # 8 개 단위 패턴 반복
    pattern_3 = [3,3,1,1,2,2,4,4,5,5] # 10 개 단위 패턴 반복
    
    # 각 학생의 점수 변수 초기화
    score_1, score_2, score_3 = 0, 0, 0
    
    # 정답 배열과 일일이 비교하면서 각 학생의 점수를 count한다
    for i in range(len(answers)):
        if answers[i] == pattern_1[i % 5]:
            score_1 += 1
        if answers[i] == pattern_2[i % 8]:
            score_2 += 1
        if answers[i] == pattern_3[i % 10]:
            score_3 += 1
    
    # 가장 높은 점수를 받은 학생 고르기
    top_score = max(score_1, score_2, score_3)
    
    # 출력 형식에 맞게, 오름차순에 맞게, return 할 answer 값 정해주기
    if top_score == score_1:
        answer.append(1)
    if top_score == score_2:
        answer.append(2)
    if top_score == score_3:
        answer.append(3)
    
    
    return answer
