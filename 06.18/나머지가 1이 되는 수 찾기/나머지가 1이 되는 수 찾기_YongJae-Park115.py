def solution(n):
    answer = 0
    for i in range(1,n):
    # n 이하 자연수 for문 돌림
        if n%i == 1:
        # n에서 1를 나눴을 때 나머지가 1이라면
            answer = i
            # answer에 i 입력
            break
            # 최저값 하나만 찾으면 되므로 바로 탈출
            # 1부터 오름차순으로 돌아가기 때문에 가장 먼저 나오고 탈출하면 최저값만 입력됨
    return answer