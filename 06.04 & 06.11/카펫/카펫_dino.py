'''sketch
종이에 그려봤음.

'''

def solution(brown, yellow):
    answer = [0, 0]
    total = brown + yellow
    # w >= h 니까, w 부터 생각하고 h를 구하면서 순회, 큰수부터 작은수로.
    for w in range(total, 2, -1):
        #  w로 나누어 떨어지는 h 구하고,
        if total % w == 0:
            h = total // w
            # 테두리 길이인 2 만큼 뺸 후의 넓이가 yellow의 면적과 같으면 문제 조건 성립. 해당 값 바로 return해서 빠져나가기
            if yellow == (w-2) * (h-2):
                answer = [w, h]
                return answer
