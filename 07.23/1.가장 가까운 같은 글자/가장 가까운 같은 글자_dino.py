def solution(s):
    answer = []

    dic = {}

    for idx, word in enumerate(list(s)):
        if word not in dic:
            answer.append(-1)
            # 해당 알파벳이 등장하는 인덱스번호를 저장
            dic[word] = idx
        else:
            answer.append(idx - dic[word])
            # 마지막으로 해당 알파벳이 등장하는 인덱스번호를 갱신 -> 그래야 제일 가까운 번호를 찾는다
            dic[word] = idx

    return answer