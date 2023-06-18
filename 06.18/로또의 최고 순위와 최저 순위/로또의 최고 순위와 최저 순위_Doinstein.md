```python
def solution(lottos, win_nums):
    rank = [1,2,3,4,5,6,6]
    ans = 6
    for x in lottos:
        if x in win_nums:
            ans-=1
    z = lottos.count(0)
    return [rank[ans-z],rank[ans]]
```