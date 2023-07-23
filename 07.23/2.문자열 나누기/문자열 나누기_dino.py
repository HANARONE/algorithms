'''
문제가 뭘 하라는 건지 이해하는데 시간을 소요했다
'''


def solution(s):
    answer = 0
    cnt1, cnt2 = 0, 0

    for i in s:
        if cnt1 == cnt2:
            answer += 1
            x = i

        if i == x:
            cnt1 += 1
        else:
            cnt2 += 1

    return answer