def solution(players, callings):
    pDict = {p:i for i,p in enumerate(players)}
    
    for call in callings:
        i = pDict[call]
        pDict[call]-=1
        pDict[players[i-1]]+=1
        players[i-1],players[i] = players[i],players[i-1]
        
        
    return players