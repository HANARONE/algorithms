def solution(s):
    answer = []
    s_dict = {x:-1 for x in set(s)}

    for i in range(len(s)):
        if s_dict[s[i]] == -1:
            answer.append(-1)
        else:
            answer.append(i-s_dict[s[i]])
        s_dict[s[i]] = i
            
    return answer