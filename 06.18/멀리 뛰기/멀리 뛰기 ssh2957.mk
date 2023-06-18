```python
#규칙을 써보다 피보나치수열임을 알게되어서 아래와 같이 짯음
def solution(n):
    if n == 1:
        return 1
    
    if n == 2:
        return 2
    
    return (solution(n-2) + solution(n-1)) % 1234567

answer = solution(n)
return answer
#근데 시간초과 발생 찾아보니 n이 엄청커지면 그 값을 컴퓨터에 저장해주면 시간을 줄여준다는 강사님의 말이 생각나서 앞의 값들을 새로운 리스트에 넣어주기로함 
def solution(n):
    arr = [0] * (n + 1) #0인 항을 n+1개만큼 만듬 사실 n개 만들어도 되지만 보기 쉽게 하기위해서 이렇게 함 
    arr[1] = 1
    arr[2] = 2
    # 1과2는 그냥 넣어준다 
    for i in range(3, n + 1):
        #덕분에 3부터 시작해서 아래값들을 넣어줌 이제 arr에는 차곡차곡 값들이 저장될거임 
        arr[i] = (arr[i - 2] + arr[i - 1]) % 1234567
       #마지막으로 n번째 있는 애를 소환해주면 끝 근데 여기서 조건이 1234567 나머지값이라고 했으니깐
    # 1324657를 나누어 준다.
    return arr[n]

    answer = solution(n)
    return answer
```

