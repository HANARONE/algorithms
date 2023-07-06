def solution(wall):
    # 파일 위치 저장할 배열
    a, b = [], []
    for i in range(len(wall)):
        for j in range(len(wall[i])):
            if wall[i][j] == "#":
                a.append(i)
                b.append(j)

    # 제일 작은 좌표부터 제일 큰 좌표까지 포함하면 전체 파일을 커버할 수 있다
    answer = [min(a), min(b), max(a) + 1, max(b) + 1]