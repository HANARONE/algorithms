from itertools import permutations
from math import sqrt

def solution(numbers):
    n = list(numbers) # 하나의 문자열 숫자를 리스트로 나누기
    p_list = [] # 소수 담을 리스트 초기화
    
    for i in range(1,len(n)+1): # 숫자 1개부터~ n개까지 순열을 위한 반복분
        for j in permutations(n,i): # i개 조합의 순열
            tmp = int(''.join(j)) # 튜플 형태의 순열을 하나의 문자열로 바꾼후 int타입으로 변경
            if tmp in [0,1]: # 소수가 아닌 0 1 제외
                continue
            elif tmp in [2,3]: # 소수인 2 3 인경우 바로 추가
                p_list.append(tmp)
            else:
                tmp_ch = True # 소수인지 체크용
                for i in range(2,int(sqrt(tmp))+1): # 2부터 tmp의 제곱근까지 
                    if tmp%i==0: # i가 tmp의 약수인 경우
                        tmp_ch = False # 소수아님
                        break # 반복문 종료
                if tmp_ch: # 소수인 경우
                    p_list.append(tmp) # 소수 리스트에 추가
    
    return len(set(p_list)) # 중복 제거된 소수 리스트의 개수