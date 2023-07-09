'''sketch
시초 없이 한 번에 풀어보자

앞 자리일수록 큰 숫자가 와야한다

마지막 value가 push 할 value보다 작다면
=> 같거나 큰 값이 나올 때까지 pop
=> O(N)

'''

def solution(number, k):
    answer = []

    for num in number:
        # 아직 숫자를 뽑아낼 기회가 남아있고, 뽑아낼 숫자 후보도 남아있는데
        # answer 리스트의 마지막 값이 push할 value인 num보다 작다면 해당 마지막 값을 pop
        # 하고 숫자를 뽑아낼 기회를 하나 날려준다
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1

        # k개의 숫자를 다 골라냈다면 정답 배열에 저장해준다
        answer.append(num)

    return ''.join(answer[:len(answer) - k])