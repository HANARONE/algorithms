def solution(sequence, k):
    n = len(sequence) # 처음부터 끝까지 확인하기 위한 sequence 길이
    end = 0 # 오른쪽(끝) 투포인터 초기화
    cnt = 1e9 # 최소 수열 길이를 위해 큰 숫자로 초기화 
    interval_sum = 0 # **부분수열의 합 > 매번 sum(sequence[start:end])으로 계산 시 시간초과
    
    # 처음부터 끝까지 반복문
    for start in range(n):
        # end가 끝부분이 아니거나 부분 수열의 합이 k보다 작은 경우
        while end<n and interval_sum < k:
            interval_sum += sequence[end] # 부분 수열에 더하기 
            end +=1 # 끝 투포인터 오른쪽으로 한칸 이동
        
        # 부분 수열 구간 합이 k 이고 길이가 이전보다 짧은 경우
        if interval_sum==k and (end-start-1) < cnt: 
            ans = [start,end-1] # 정답
            cnt = end-start-1 # 최소 길이 
            
        interval_sum-=sequence[start] # 시작 투포인터 값 지우기 = 오른쪽으로 한 칸 이동
    return ans