def solution(lottos, win_nums):
# 내 로또번호와 당첨번호 매개변수 리스트
    answer = []
# 최고순위와 최저순위 들어갈 리스트
    top = 0
# 당첨번호 최대 갯수
    low = 0
# 당첨번호 최저 갯수
    for i in lottos:
    # 내 로또번호들 중에서
        if i == 0:
    # 지워진 번호 있을시
            top += 1
    # 지워진 번호가 다 당첨번호라고 가정하고 최대 갯수 추가
        for j in win_nums:
        # 당첨번호 값들 중에서
            if i == j:
            # 지워지지 않은 내 번호와 당첨번호가 같은게 있다면
                top += 1
                # 가능한 최대 개수 + 1
                low += 1
                # 가능한 최저 개수 + 1
    if top < 2:
    # 최대 개수가 2개 미만이면, 당연히 최저개수도 2개 미만이고
    # 등수는 6등
        answer.append(6)
        # 최고 등수 추가
        answer.append(6)
        # 최저 등수 추가
    elif low < 2:
    # 최저 당첨 개수가 2 미만일시 최대 당첨개수는 2개 이상일 수 있음
        answer.append(7-top)
        # 최고 등수 추가
        answer.append(6)
        # 최저 등수 추가
    else:
    # 최대 당첨개수, 최저 당첨개수 모두 2 넘어갈 때
        answer.append(7-top)
        # 최고 등수 추가
        answer.append(7-low)
        # 최저 등수 추가
    return answer