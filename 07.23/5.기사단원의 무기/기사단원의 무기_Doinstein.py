def divisor(n):
    tmp = []
    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            tmp.append(i) 
            if ((i**2)!=n):
                tmp.append(n//i)
    tmp.sort()
    return tmp

def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        tmp = divisor(i)
        if len(tmp)>limit:
            answer+=power
        else:
            answer+=len(tmp)
    return answer