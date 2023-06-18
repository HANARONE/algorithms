```python
from itertools import combinations
from collections import Counter
def solution(orders, course):
    result = []
    
    for i in course:
        tmp = []
        for order in orders:
            tmp += list(map(lambda x: ''.join(sorted(x)),combinations(order,i)))
        
        sorted_tmp = Counter(tmp).most_common()
        result += [a for a,b in sorted_tmp if b > 1 and b == sorted_tmp[0][1]]
        
    return sorted(result)
```