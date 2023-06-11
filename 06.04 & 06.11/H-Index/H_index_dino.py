def solution(citations):
    # 정렬해주고
    citations.sort()
    # 다 순회 , 완전탐색하는데
    for i in range(len(citations)):
        # 조건에 맞다면
        if citations[i] >= len(citations) - i:
            return len(citations) - i
        
    # 위에거를 다 스루했다면 0 return
    return 0
