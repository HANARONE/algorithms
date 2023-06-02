from itertools import product
def solution(word):
    alphabet_list = ['A', 'E', 'I', 'O', 'U'] # 알파벳 모음
    p_list = [] # 사전 초기화
    for i in range(1,6): # 길이 1부터 5까지 반복문
        tmp = list(product(alphabet_list,repeat=i)) # i 길이의 알파벳 중복 순열
        p_list.extend(list(map(lambda x: ''.join(x),tmp))) # 사전에 추가
    
    return sorted(p_list).index(word)+1 # 정렬 후 word의 인덱스 + 1
