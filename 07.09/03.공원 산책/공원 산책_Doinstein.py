def solution(park, routes):
    n,m = len(park),len(park[0])
    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                s = [i,j]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    d = ['E','W','S','N']
    for route in routes:
        r,t = route.split(' ')
        t = int(t)
        rx = dx[d.index(r)]
        ry = dy[d.index(r)]
        nx,ny = s
        
        while t:
            if 0<=nx+rx<n and 0<=ny+ry<m and park[nx+rx][ny+ry] != 'X':
                t-=1
                nx+=rx
                ny+=ry
            else:
                break
        
        if t == 0:
            s = [nx,ny]
            print(s)
    return s