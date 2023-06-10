def solution(brown, yellow):
    answer = []
    k = []
    # yellow 사각형의 가로 세로 들어갈 리스트 k 만듦
    for i in range(1,yellow+1):
        if yellow%i == 0:
            # yellow 사각형의 변이 정수로 떨어지면
            k.append([i,yellow//i])
            # k에 리스트 추가
    for i,j in k:
        # k에 있는 리스트 (= yellow의 가로,세로)
        if brown == 2*i +2*j + 4:
            # brown이 yellow 사각형 덮어야 되므로 2*i + 2*j + 4가 brown의 수와 같다면
            return(max(i+2,j+2),min(i+2,j+2))
            # 답 출력
            
    
    return answer