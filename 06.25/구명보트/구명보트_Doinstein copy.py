from collections import deque
def solution(people, limit):
    people.sort()
    ans = 0
    people = deque(people)
    while len(people)>1:
        # print(people)
        if people[0]+people[-1]<=limit:
            ans+=1
            people.popleft()
            people.pop()
        else:
            ans+=1
            people.pop()
    
    if people:
        # print(people)
        return ans+1
    return ans