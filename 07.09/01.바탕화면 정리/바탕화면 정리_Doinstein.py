def solution(wallpaper):
    n,m = len(wallpaper),len(wallpaper[0])
    result = [1e9,1e9,0,0]
    
    for i in range(n):
        for j in range(m):
            if wallpaper[i][j] == '#':
                result[0] = min(result[0],i)
                result[1] = min(result[1],j)                
                result[2] = max(result[2],i+1)                
                result[3] = max(result[3],j+1)
    return result