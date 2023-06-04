def solution(numbers):
    sn = list(map(lambda x: str(x),numbers)) # 숫자 문자열로 변경
    sn.sort(key=lambda x: (x*4)[:4], reverse=True)
    # 1000이하 원소 > 최대 4자리로 맞춘 값을 기준으로 정렬
    
    answer = ''.join(sn) # 리스트 하나의 문자열로 합치기 
    
    if set(answer) == {'0'}: # 모든 숫자가 0일 경우 0으로 출력
        return '0'
    else:
        return answer   