def solution(answers):
# answers 는 문제에서 주어진 데이터
    answer = []
# 찍는 방식 고정
    first_babo = [1,2,3,4,5]
    second_babo = [2,1,2,3,2,4,2,5]
    third_babo = [3,3,1,1,2,2,4,4,5,5]
# 맞춘 개수 담을 점수판 만들기
    score = [0,0,0]
    
    for i,v in enumerate(answers):
# 답안지 인덱스와 값 for문 돌리기
        if v == first_babo[i % 5]:
# 답(v)이 첫학생이 찍은 답과 같다면 
# ※ 찍는 주기가 5이므로 순차적으로 출력되는 first_babo 인덱스값의 나머지로 firtst_babo의 답 출력 
            score[0] += 1
# score에 점수 추가
    for i,v in enumerate(answers):
        if v == second_babo[i % 8]:
            score[1] += 1
    for i,v in enumerate(answers):
        if v == third_babo[i % 10]:
            score[2] += 1
# second_babo, third_babo 돌리는 방식 first_babo와 동일
# 인덱스 값 지정은 찍는 주기에 맞게
    
    for i,v in enumerate(score):
# 스코어 리스트의 인덱스, 값 에서 for문 돌리기
        if v == max(score):
# 위에서 합산한 스코어의 값 제일 높은애한테
            answer.append(i+1)
# answer에 값 추가
# +1 하는 이유는 인덱스이기 때문에 0부터 시작하지만 첫번째 학생을 출력하려면 0이 아닌 1이 나와야 한다
    return answer


# enumerate() 함수는 인덱스와 주어진 값을 동시 출력, 알고리즘 문제 풀 때 요긴하게 써먹는다고 한다.