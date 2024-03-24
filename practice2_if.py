# @@@ 조건문 @@@

#1330
A,B = map(int, input().split())
if (A>B):
    print(">")
elif(A<B):
    print("<")
else:
    print('==') #같은거 표시할떄는 ==


#9498
a = int(input())

if(90<=a<=100):
    print("A")
elif(80<=a<=89):
    print("B")
elif(70<=a<=79):
    print("C")
elif(60<=a<=69):
    print("D")
else:
    print("F")


#2753
a= int(input())
if(a%4==0) and (a%100!=0):
    print("1")
elif(a%400 ==0):
    print("1")
else: print("0")


#14681
x = int(input())
y = int(input())

if (x>0):
    if (y>0):
        print("1")
    else:
        print("4")
else:
    if (y>0):
        print("2")
    else:
        print("3")


#2884
H, M = map(int, input().split())
if M<45:
    M += 15
    if H==0:
        H=23
    else:
        H -=1
else:
    M -=45
print(H, M)


#2525
h,m = map(int, input().split()) # 시작 시 분
time = int(input()) # 걸리는 시간
ov_time = 0

if (m+time <= 59):
    m += time
elif (m+time>=60):
    ov_time = m +time
    h += int((m+time)/60)
    m = ov_time - int((m+time)/60)*60
    if (h>=24):
        h = h-24
print(h,m)

#2480
a,b,c = map(int, input().split())
if(a==b==c):
    print(10000+a*1000)
elif(a==b or a==c):
    print(1000 +a*100)
elif b==c:
    print(1000 +b*100)
else:
    print(max(a,b,c)*100)
