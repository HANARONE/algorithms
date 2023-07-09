def hanoi(n,start,end,aux):
    if n==1 :
        return [[start,end]]
    return hanoi(n-1,start,aux,end)+[[start,end]]+hanoi(n-1,aux,end,start)

def solution(n):
    answer = hanoi(n,1,3,2)
    return answer