def solution(array, commands):
    return [sorted(array[c[0]-1:c[1]])[c[2]-1] for c in commands]
# commands를 반복문으로 하나씩 출력
# 문제에서 첫 번째가 1부터 시작하기 때문에 인덱스에 -1