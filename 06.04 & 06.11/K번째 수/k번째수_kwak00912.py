def solution(array, commands):
    result = []
      
    for l in range(len(commands)):
        arr = commands[l]
        i = arr[0]
        j = arr[1]
        k = arr[2]
                
        # i부터 j까지 슬라이싱 + 정렬
        arr_ = []
        arr_ = sorted(array[i-1:j:1])
        
        # k번째 숫자 구하기
        m = arr_[k-1]
        result.append(m)

        
    return result
