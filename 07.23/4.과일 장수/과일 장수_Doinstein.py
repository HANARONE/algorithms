def solution(k, m, score):
    ans=0
    score.sort(reverse=True)
    n = len(score) - len(score)%m
    for i in range(m,n+1,m):
        ans+=(score[i-1])*m
    return ans