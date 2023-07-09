def solution(park, routes):
    lenx = len(park)
    leny = len(park[0])
    lenr = len(routes)
    
    # 범위 안에 있는 지 확인하는 함수
    def in_range(x, y):
        return x >= 0 and y >= 0 and x < lenx and y < leny
    
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    
    # 시작 x, y 찾기
    for i in range(lenx):
        for j in range(leny):
            if park[i][j] == "S":
                x, y = i, j
                break
                
    for i in range(lenr):
        a, b = (routes[i].split())
        b = int(b)
        if a == "E":
            d_num = 0
        elif a == "S":
            d_num = 1
        elif a == "W":
            d_num = 2
        else:
            d_num = 3
        
        # 조건에 따라 이동하기
        # 임시 x, y 생성
        YN = True
        tmpx, tmpy = x, y
        for j in range(b):
            nx, ny = tmpx + dxs[d_num], tmpy + dys[d_num]
            
            if in_range(nx, ny) and park[nx][ny] != 'X':
                tmpx, tmpy = nx, ny
                
            else:
                YN = False
                break
        
        # 전부 정상적으로 이동했다면 x, y 값 변경
        if YN:    
            x, y = tmpx, tmpy
            
            
    answer = [x, y]
            
    return answer