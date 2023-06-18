# 로또 당첨 등수 리턴하는 함수 정의
def rank(cnt):
    if cnt < 2:
        return 6
    elif cnt == 2:
        return 5
    elif cnt == 3:
        return 4
    elif cnt == 4:
        return 3
    elif cnt == 5:
        return 2
    else:
        return 1

# 최고 순위, 최저 순위 리턴하는 함수
def solution(lottos, win_nums):
    answer = []
    empty = 0
    w_cnt = 0
    
    for i in range(6):
        if lottos[i] == 0:
            empty += 1
        else:
            for j in range(6):
                if lottos[i] == win_nums [j]:
                    w_cnt += 1
    # 일치 횟수 = 최소 일치 횟수
    min_cnt = w_cnt
    # max = 일치 횟수 + 알아볼 수 없는 숫자
    max_cnt = w_cnt + empty
    
    answer = (rank(max_cnt), rank(min_cnt))
        
    
    
    return answer