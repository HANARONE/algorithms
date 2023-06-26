def solution(keymap, targets):
    alpha_list = set(''.join(keymap))
    ans = []
    alpha_dict = {}
    for a in alpha_list:
        if a not in alpha_dict:
            alpha_dict[a] = 1e9

    for k in keymap:
        for a in k:
            alpha_dict[a] = min(alpha_dict[a], k.index(a)+1)
            
    for target in targets:
        tmp = 0
        for t in target:
            if t not in alpha_list:
                tmp = -1
                break
            tmp+=alpha_dict[t]
        ans.append(tmp)
    
    return(ans)