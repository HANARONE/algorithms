def solution(n):
    answer = 0
    
    # 조건을 만족하는 가장 작은 수를 찾아야하므로 2부터 먼저 탐색한다
    for x in range(2, n):
        # 조건을 만족한다면 바로 break하여 for문을 벗어나게 해준다
        if n % x == 1:
            answer = x
            break
    
    return answer
