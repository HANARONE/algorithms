n = int(input())
nlist = sorted(list(map(int, input().split())))
x = int(input())

result = 0
idx, idy = 0, n - 1

while True:
    a = nlist[idx]
    b = nlist[idy]
    
    if idx >= idy:
        break
    
    if a + b == x:
        result += 1
        idx += 1
        idy -= 1
    
    elif a + b < x:
        idx += 1
    
    elif a + b > x:
        idy -= 1
        
print(result)
    

