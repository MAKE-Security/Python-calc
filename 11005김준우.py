num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))
operator = input("연산자를 입력하세요 (+, -, *, /): ")

# 연산 수행
if operator == "+":
    result = num1 + num2   ##operator은 파이썬의 내장 연산자에 해당하는 효율적인 함수 집합을 내보냅니다. 
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("잘못된 연산자 입력입니다.")
    result = None

# 결과 출력
if result is not None:
    print("결과: ", result)
    
    
    
