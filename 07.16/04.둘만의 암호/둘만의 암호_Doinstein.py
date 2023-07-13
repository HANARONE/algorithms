def solution(s, skip, index):
    alpha = ''.join([chr(i) for i in range(97,123)])
    for i in skip:
        alpha = alpha.replace(i,'')
    ans = ''
    for x in s:
        ans+= alpha[(alpha.index(x)+index)%len(alpha)]
    return ans