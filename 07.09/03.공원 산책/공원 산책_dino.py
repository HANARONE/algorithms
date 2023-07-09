def solution(park, routes):
    x, y = 0, 0
    row, col = len(park[0]), len(park)
    dir = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}

    # 시작점
    for i in range(col):
        for j in range(row):
            if park[i][j] == "S":
                x, y = i, j
                break

    # 좌표이동
    for r in routes:
        dist, num = r.split(" ")
        num = int(num)
        dx, dy = x, y

        for i in range(num):
            nx = x + dir[dist][0]
            ny = y + dir[dist][1]

            # 이동할 좌표가
            # 1. 보드 안에 있으면서 & 2. 장애물이 없다는 제한 조건 성립 시 좌표 이동
            if 0 <= nx <= col - 1 and 0 <= ny <= row - 1 and (park[nx][ny] != "X"):
                x, y = nx, ny

            # 제한 조건에 걸린다면 좌표 이동 없이 현재 위치 그대로 둔 다음 loop문을 돈다
            else:
                x, y = dx, dy
                break

    return [x, y]