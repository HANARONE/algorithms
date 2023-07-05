def solution(name, yearning, photo):
    sDict = {x:y for x,y in zip(name,yearning)}
    result = []
    for pho in photo:
        tmp = [sDict[x] if x in sDict else 0 for x in pho ]
        result.append(sum(tmp))
        
    return result