def solution(scores):
    w = scores[0] # 완호 점수
    sum_w = sum(w) # 완호 점수의 합
    scores.sort(key = lambda x: (-x[0],x[1])) # **왼쪽 내림차순 후 오른쪽 오름차순 정렬
    ans = 1 # 등수 초기화
    maxb = 0 # 오른쪽 점수의 최대 값
    
    # 모든 경우의 수를 다 비교하는 것은 비효율적
    # 크기를 비교하기 때문에 정렬을 통해 경우의 수를 줄이기
    for score in scores:
        if sum_w >= sum(score): # 완호보다 점수가 낮은 경우는 제외
            continue
        if w[0] < score[0] and w[1] < score[1]: # 완호의 두 점수가 모두 낮은 경우
            return -1
        if maxb <= score[1]:
            maxb = score[1]
            ans +=1
            
    # score[0]은 내림차순이기 때문에 이전 값보다 작거나 같다
    # score[1]은 오름차순이기 때문에 score[0]이 동일하면 score[1]은 이전 값보다 크거나 같다
    # 반복문에서 score[0]은 이전 값보다 무조건 작기 때문에 최대값(maxb)이 score[1]보다 큰 경우
    # score[0]과 score[1] 모두 낮은 경우가 된다 > if maxb <= score[1] > Flase

    return ans