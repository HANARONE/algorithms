def solution(keymap, targets):
    answer = []
    key_dict = {}
    # keymap의 패턴과 min(index)을 key_dict라는 딕셔너리에 저장
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            # print(keymap[i][j])
            char = keymap[i][j]
            if char not in key_dict:
                key_dict[char] = j + 1
            # 만약 key_dict에 이미 있다면 비교해서 최소 인덱스값을 저장
            else:
                key_dict[char] = min(key_dict[char], (j + 1))
    # print(key_dict)

    # 검증하려는 패턴마다 최소 몇 번씩 눌러야 하는지 answer 배열에 저장
    for target in targets:
        # targets 배열의 한 패턴마다 최소 누르는 횟수를 더하는 cnt 값 초기화
        cnt = 0
        for t in target:
            # key_dict 에서 해당 알파벳을 찾았다면 최소 누르는 횟수를 cnt에 저장해준다
            if t in key_dict:
                cnt += key_dict[t]
            # key_dict 에서 해당 알파벳이 없다면 목표 문자열을 작성할 수 없으므로 바로 cnt 에 -1을 할당해주고 for loop문을 탈출한다
            else:
                cnt = (-1)
                break
        # 패턴 하나 끝날 때마다 최소 누를는 횟수를 다 합한 cnt 값을 answer배열에 더해준다
        answer.append(cnt)

    return answer