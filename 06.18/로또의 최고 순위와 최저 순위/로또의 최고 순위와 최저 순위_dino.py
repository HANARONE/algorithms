def solution(lottos, win_nums):
    answer = []
    # 알아볼 수 없는 번호의 개수 => 잠재적으로 맞출 수도 있음
    cnt = 0
    # 현재 확실하게 맞춘 번호의 개수
    result = 0
    # 맞춘 번호의 개수에 따른 순위를 인덱스 번호로 갖는 ranks 리스트
    ranks = [6,6,5,4,3,2,1]
    
    for num in lottos:
        # 번호를 맞췄다면 result 에 확실하게 맞춘 개수에 카운트
        if num in win_nums:
            result += 1
        # 0이라면 아직 맞췄는지 아닌지 모르는 갯수 cnt에 카운트
        if num == 0:
            cnt += 1
    
    # 맞춘 번호의 개수를 인덱스번호 삼아서 ranks에서 value로 순위를 가져온다
    min_rank = ranks[result]
    max_rank = ranks[result + cnt]
    
    # return 형식
    answer = [max_rank, min_rank]
    
    return answer
