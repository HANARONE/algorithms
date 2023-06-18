def solution(n):
    answer = 0
    # 나머지가 1이 되는 수 중 가장 큰 수는 n-1이므로, 1에서 n까지로 범위 정함
    for i in range(1, n):
        if n % i == 1:
            answer = i
            return answer