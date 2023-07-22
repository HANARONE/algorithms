def solution(s):
    ans = []
    cnt1,cnt2 = 0,0
    c = 0
    for i in range(len(s)):
        if s[c] == s[i]:
            cnt1+=1
        else:
            cnt2+=1
        if cnt1==cnt2:
            ans.append(s[c:i+1])
            c = i+1
            
    if c < len(s):
        ans.append(s[c:])
    return len(ans)