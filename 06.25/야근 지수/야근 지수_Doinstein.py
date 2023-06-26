from heapq import heapify,heappush,heappop
def solution(n, works):
    works = [-work for work in works]
    heapify(works)
    
    while n:
        post = heappop(works)
        curr = post+1
        heappush(works,curr)
        n-=1
    
    return sum([i**2 for i in works if i <0])