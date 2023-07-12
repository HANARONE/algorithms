def solution(n, m, section):
    if m == 1:
        return len(section)
    else:
        ans=1
        c = section[0]
        for s in section[1:]:
            if c+m-1 < s:
                c = s
                ans+=1
        return ans