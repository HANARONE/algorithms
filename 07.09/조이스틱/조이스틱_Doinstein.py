def solution(name):
    if set(name) == {'A'}:
        return 0

    answer = 1e9
    for i in range(len(name) // 2): # 반 이상 움직일 필요 없음 > 왼쪽반+오른쪽반
        left_moved = name[-i:]+name[:-i] # 왼쪽으로 i칸까지
        right_moved = name[i:]+name[:i] # 오른쪽으로 i칸까지
        print(i,' ',left_moved)
        print(i,' ',right_moved[0]+right_moved[:0:-1])
        for n in [left_moved, right_moved[0]+right_moved[:0:-1]]:
            while n and n[-1] == 'A':
                n = n[:-1] 

            row_move = i + len(n)-1
            col_move = 0
            for c in map(ord, n):
                col_move += min(c - 65, 91 - c)

            answer = min(answer, row_move + col_move)

    return answer