def cal(x):
    a,b=x
    return (a*60)+b

def solution(plans):
    ps = list(map(lambda x: [x[0],cal(map(int,x[1].split(':'))),int(x[2])],plans))
    ps.sort(key=lambda x: x[1])
    p_dict = {x:z for x,y,z in ps}
    
    stoped = []
    ans = []
    
    now = ps[0][1]+ps[0][2]
    for i in range(1,len(ps)):
        nxt = ps[i][1]
        if now <= nxt:
            t = nxt-now
            ans.append(ps[i-1][0])
            
            while t > 0 and stoped:
                tmp = t
                t-=p_dict[stoped[-1]]
                p_dict[stoped[-1]]-=tmp
                if p_dict[stoped[-1]] <= 0:
                    ans.append(stoped.pop())
        else:
            t = now-nxt
            stoped.append(ps[i-1][0])
            p_dict[ps[i-1][0]]=t
        now = nxt+ps[i][2]
        
    ans.append(ps[-1][0])
    ans+=stoped[::-1]
    return ans