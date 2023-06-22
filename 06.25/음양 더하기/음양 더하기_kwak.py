def solution(absolutes, signs):
    answer = 0
    
    for i in range(len(absolutes)):
        if signs[i]: #signs[i]가 true면
            absolutes[i] = absolutes[i] # 양수라는 뜻이므로 변경 없음
        else:
            absolutes[i] = absolutes[i] * -1 # 음수라는 뜻이므로 -1을 곱함
        
    answer = sum(absolutes) # 전체 합
    
    return answer
