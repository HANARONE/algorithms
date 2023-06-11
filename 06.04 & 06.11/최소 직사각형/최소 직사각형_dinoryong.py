def solution(sizes):
    answer = 0
    temp = []
    temp2 = []

    # 2차원 배열 sort할 경우 결과는
    # sizes.sort(reverse=True)
    # print(sizes)

    # 2차원 배열에서 주의 . max도 첫번째원소에만 먹힌다
    # print(max(sizes))

    # 큰 값 중에 큰 값, 작은값들 중에서 큰 값
    for i in range(len(sizes)):
        temp.append(max(sizes[i]))
        temp2.append(min(sizes[i]))

    answer = max(temp) * max(temp2)

    return answer
