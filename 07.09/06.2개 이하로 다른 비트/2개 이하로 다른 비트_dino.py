'''sketch
직접 써보면서 관찰
1. x 의 비트를 1개 바꾸는 case
x보다 큰 수들 중에서, 조건을 만족하는 가장 작은 수
=> 0을 1로 딱 한 번 봐꿔야 하는데, 그 중에 가장 작은 수여야 하기 때문에
x의 0 중에서 가장 차수가 낮은 자리를 바꿔준다
&
x가 짝수이면 가장 마지막 자리 비트가 0이기 때문에 이 case

2. x 의 비트를 2개 바꾸는 case
x가 홀수이면 가장 마지막 자리 비트가 1이기 때문에 이 case
1개 : 0 => 1 : 가장 뒷자리에 있는 0 을 n번째 자리에서 바꿨음
1개 : 1 => 0 : (n - 1) 번째 자리부터 낮은 자리로 탐색하면서 가장 높은 자리의 1을 0으로 바꿔준다

int(숫자,base)
=> binary to integer
'''
def int_to_bin(x):
    temp = []

    while True:
        remainder = x % 2
        x //= 2
        temp.append(remainder)

        if x < 2:
            temp.append(x)
            break
    temp.reverse()
    answer = "".join(map(str, temp))

    return answr

def solution():
    answer = []

    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)
            continue

        else:
            bin_num = int_to_bin(num)
            if not '0' in bin_num:
                answer.append(int('10' + bin_num[1:], 2))
            else:
                # 가장 낮은 자리부터 0비트를 찾는다
                idx = bin_num.rfind('0')
                answer.append(int(bin_num[:idx] + '10' + bin_num[idx + 2:], 2))

    return answer


'''sketch
늘 내가 피하는 비트마스킹 풀이도 있다

'''
