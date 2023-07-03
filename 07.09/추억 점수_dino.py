def solution(name, yearning, photo):
    answer = []
    # 각 사람별 추억점수를 저장해줄 dictionary 형성
    dict = {}
    for n in range(len(name)):
        dict[name[n]] = yearning[n]

    print(dict)

    for ph in photo:
        cnt = 0
        for person in ph:
            # dict에 있는 경우에만 추억 점수를 올려준다
            if person in dict:
                cnt += dict[person]
            else:
                pass

        # 각 사진마다 추억점수를 answer 배열에 저장한다
        answer.append(cnt)

    return answer