def solution(keymap, targets):
    answer = []
    for i in targets():
        for j in range(len(i)):
            a = i[j:j+1]
            for k in keymap:
                for l in range(len(k)):
                    b = k[l:l+1]
                    if a == b:
    return answer

# 수도코드
# targets에 있는 문자 순서대로 확인
# 글자 해당값이 keymap 리스트 값에 있는지 for문으로 다 돌려보기
# 리스트 값에 여러개 있다면 최소 번호를 추출, 하나만 있으면 바로 추출
# 문자열이 없다면 -1 저장후 탈출
# 최소번호 나온 값들 다 더하고 answer 리스트에 집어넣기

# 진짜 막썼습니다