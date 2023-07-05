import math
def cal(x):
    if x == 1:
        return 0
    else:
        ans = [1]
        for i in range(2,int(math.sqrt(x))+1):
            if x%i == 0 and i <=1e7:
                ans.append(i)
                if x//i <=1e7:
                    ans.append(x//i)

        return max(ans)
        
def solution(begin, end):
    return [cal(i) for i in range(begin,end+1)]