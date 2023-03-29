first = int(input('두번째 숫자를 입력하세요:'))
op = input('연산자를 입력하세요:')
second = int(input('두번째 숫자를 입력하세요:'))

if op == '+':
    print(first + second)
elif op == '-':
    print(first - second)
elif op == '*':
    print(first * second)
elif op == '/':
    if second == 0:
        print("0으로 나눌수 없습니다")
    else:
        print(first / second)
else:
    print('잘못 입력하였습니다')
