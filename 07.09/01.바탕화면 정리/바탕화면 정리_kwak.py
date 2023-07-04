import sys

def solution(wallpaper):
    # 변수 선언 및 입력:
    x_len = len(wallpaper) # 세로 길이
    y_len = len(wallpaper[0]) # 가로 길이
    min_x, min_y = sys.maxsize, sys.maxsize # 비교값 생성
    max_x, max_y = -1, -1
    
    for i in range(x_len):
        for j in range(y_len):
            if wallpaper[i][j] == "#":
                min_x = min(i, min_x)
                min_y = min(j, min_y)
                max_x = max(i, max_x)
                max_y = max(j, max_y)	
                
    return [min_x, min_y, max_x+1, max_y+1]