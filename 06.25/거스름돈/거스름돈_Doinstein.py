def solution(n, money):
    dp = [1] + [0] * n  # 동전 조합의 개수를 저장하는 DP 리스트 초기화
    
    for coin in money:
        for i in range(coin,n+1):
            dp[i] = (dp[i] + dp[i - coin])%1000000007
    # coin을 동전으로 사용할 때, i 금액을 만들 수 있는 조합의 수를 업데이트
    
    return dp[n]  # n 금액을 만들 수 있는 조합의 수 반환

# 참고 - https://yejin72.tistory.com/35