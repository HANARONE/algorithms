# 중복순열 가져온 풀이
from itertools import product
def solution(word):
    answer = 0
    dictionary = []
    for i in range(1, 6):
        dictionary.extend(list(map(''.join, product(['A','E','I','O','U'], repeat=i))))
    dictionary.sort()
    return dictionary.index(word)+1

# A : 1, E : 782, I : 1563번째 단어, 
def solution(word):
    answer = 0
    arr = ['A', 'E', 'I', 'O', 'U']
    num = [781, 156, 31, 6, 1]
    for i in range(len(word)):
        answer += arr.index(word[i]) * num[i] + 1
    
    return answer
