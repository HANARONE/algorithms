def solution(sizes):
    w = []
    # 큰값 들어갈 리스트 만들기
    h = []
    # 작은값 들어갈 리스트 만들기
    answer = 0
    for i in range (len(sizes)):
        w.append(max(sizes[i]))
        # 가로 or 세로 중 큰값 w리스트에 추가
        h.append(min(sizes[i]))
        # 가로 or 세로 중(위에 가로면 여긴 세로) 작은값 h리스트에 추가
    answer=max(w)*max(h)
    # 큰값들(w)중 가장 큰것과 작은 값들(h)중 가장 큰것의 곱
    # h중 가장 작은값이 들어가면 h에서 그보다 큰 값을 가지는 명함을 못넣는다
    return answer