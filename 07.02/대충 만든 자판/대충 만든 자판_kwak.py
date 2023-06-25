keymap = list(input().split())
targets = list(input().split())

def solution(keymap, targets):
    answer = []
    val = -1
    
    for i in range(len(tagets)):
        idx = 0
        for j in tagets[i]:
            for k in range(len(keymap)):
                if keymap[k].find(k) > val:
                    val = keymap.find(k)
                    idx = k
                if val == -1:
                    return answer.append(-1)
                answer[] += val     
            
