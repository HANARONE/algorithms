def solution(players, callings):

    leng = len(callings) 
    for i in range(leng):
        x = callings[i]
        dx = players.index(x)
        players[dx], players[dx-1] = players[dx-1], players[dx]
        
    return players