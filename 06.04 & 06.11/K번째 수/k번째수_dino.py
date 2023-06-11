def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        # 조건대로 자르기
        arr = array[i-1:j]
        # 정렬해주고
        arr.sort()
        # k번째 숫자 골라서 배열에 추가해주기
        answer.append(arr[k-1])
    return answer
