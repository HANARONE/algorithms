# 조합,Counter 쓰면 편하지만 없이도 풀어보기~
from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    result = []
    
    for course_num in course:
        # course에 속한 단품 개수에 따라서 만들어낼 수 있는 메뉴조합을 order_combis에 저장한다
        order_combis = []
        for order in orders:
            # a = ''.join(sorted(order))
            order_combis += combinations(sorted(order), course_num)
        # print(order_combis)
        
        # Counter().most_common() 을 써서 가장 갯수가 많은 메뉴 순서대로 정렬
        most_ordered = Counter(order_combis).most_common()
        # print(most_ordered)
        
        
        # 최대갯수인 코스만 포함하기
        answer += [k[0] for k in most_ordered if (k[1] == most_ordered[0][1] and k[1] > 1)]
    
    # 출력형식에서 사전순 & join
    answer = [''.join(a) for a in sorted(answer)]
        
    return (sorted(answer))
