# 입력 받아오기
N, S = map(int, input().split())
arr = list(map(int, input().split()))

# 투포인터변수
start, end = 0, 0
sum_ans = arr[0]
ans = 100001

while True:
    if sum_ans < S:
        end += 1
        if end == N:
            break
        sum_ans += arr[end]
    else:
        sum_ans -= arr[start]
        ans = min(ans, end - start + 1)
        start += 1

print(ans if ans != 100001 else 0)