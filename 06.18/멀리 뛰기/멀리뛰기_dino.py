# 피보나치 수열 점화식 dp
def solution(n):
    if n == 1: 
        return 1
    
    else: 
        # dp 테이블 초기화
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        # 3부터 점화식 적용해서 dp 테이블 채우기
        for i in range(3, n + 1):
            dp[i] = dp[i-2] + dp[i-1]

        # dp 테이블 마지막 값 return
        return dp[-1] % 1234567
