# DICTIONARY 써야 시초 안 난다
def solution(players, callings):
    idx = {i: player for i, player in enumerate(players)}
    play = {player: i for i, player in enumerate(players)}

    for i in callings:
        rank = play[i]
        rank2 = rank - 1
        i2 = idx[rank2]

        idx[rank] = i2
        idx[rank2] = i

        play[i] = rank2
        play[i2] = rank

    answer = list(idx.values())

    return answer