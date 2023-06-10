def solution(numbers):
    answer = ''
    
    s = list(map(str,numbers))
    # numbers 문자화 하고 리스트에 저장
    s.sort(key=lambda x:x*4, reverse = True)
    # 991, 9가 동시에 있다 가정할 때 9가 991 보다 먼저 나와야 함
    # 각 문자열에 *3 해주면 991991991, 999로 돼서 9가 991보다 앞으로 정렬 될 수 있음
    # *4 인 이유는 1000이하이기 때문에 4번만 곱해주면 됨
    answer = str(int(''.join(s)))
    # 답 제출하는데 이미 문자열 상태라 (''.join(s))만 제출했는데 케이스 하나 오답뜸
    # int를 중간에 한번 왜 거쳐야 되는지 모르겠음    
    return answer