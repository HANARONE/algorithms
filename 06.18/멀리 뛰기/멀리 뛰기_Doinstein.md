```python
# 패턴을 파악하는 문제
def solution(n):
    stack = [1,1] # 피보나치 초기화
    for i in range(2,n+1):
        stack.append(stack[i-1]+stack[i-2])
        
    return stack[-1]%1234567
```