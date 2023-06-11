# 순열 함수 땡겨오기
from itertools import permutations

# 소수 판별 함수 따로 뺐음. 뭔가 코드트리 스타일로.
def is_prime_number(x) :
    # 1번. 2보다 작으면 소수가 아니다
    if x < 2 :
        return False
    
    # 2번. 2부터 x-1 까지 순회할 때, x와 나누어 떨어진다면 소수가 아니다
    for i in range(2, x) :
        if x % i == 0 :
            return False
        
    # 위 2개를 모두 통과했다면 소수이다        
    return True

def solution(numbers):
    answer = 0
    nums = []
    
    # numbers 배열에서 (1~len(numbers)) 개를 뽑아서 순열 만들고
    # 새로운 nums 배열에 저장, set 집합함수
    for i in range(1, len(numbers)+1) :
        nums.append(list(set(map(''.join, permutations(numbers, i)))))
        print(nums)
        # [['1', '0'], ['01', '11', '10'], ['110', '011', '101']]
    
    # nums의 원소를 정수형으로 바꿔서 permut 1차원 배열에 nums의 숫자들 저장, set 중복제거
    permut = list(set(map(int, set(sum(nums, [])))))
    print(permut)
#     [0, 1, 101, 10, 11, 110]
    
    # 소수 판별 함수 사용해서 True 면 return answer 값을 +1
    for elem in permut :
        if is_prime_number(elem) == True :
            answer += 1

    return answer
