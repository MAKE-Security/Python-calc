a=list(map(int,input("숫자 2개 입력하세요: ").split()))
print(a)
print("1.+\n2.-\n3.*\n4./")
c=int(input("연산자를 입력하세요: "))

if(c == 1):
    print("값:",a[0]+a[1])
if(c == 2):
    print("값:",a[0]-a[1])
if(c == 3):
    print("값:",a[0]*a[1])
if(c == 4):
    print("값:",a[0]/a[1])
