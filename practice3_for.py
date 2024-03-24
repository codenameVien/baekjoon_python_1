# @@@ 반복문 @@@
#2739
n = int(input())
for i in range(n,n+1):
    for j in range(1,10):
        print(i,"*",j,"=",i*j)


#10950
T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print(a+b) # 각 테스트 케이스마다 결과 값 출력


#8393
n = int(input())
tot = 0
for i in range(1,n+1):
    tot += i
print(tot)


#25304
X = int(input()) #총금액
N = int(input()) #구매한 물건 종류의 수
tot_price = 0

for i in range(N):
    a, b = map(int, input().split())
    tot_price += a*b

if (X == tot_price):
    print("Yes")
else:
    print("No")


#25314
N = int(input())
t= int(N/4)
print(("long "*t)+"int")

#25314 반복문 사용시
N = int(input())
t = int(N/4)
for i in range(t):
    print("long ", end="")
print("int")


# #15552 아니 이거 왜 채점 안됨? 
# T = int(input())
# for i in range(T):
#     a, b =map(int, input().split())
#     print(a+b)

#15552 sys 를 사용해보자 - 찾아보니 처리속도가 더 빠르다네요
import sys
T = int(sys.stdin.readline())
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)


# 11021
T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print("Case #{}: ".format(i+1), end="")
    print(a+b)


#11022
T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print("Case #{0}: {1} + {2} = {3}".format(i+1, a, b, a+b))


#2438
N= int(input())
for i in range(N):
    a = i+1
    print("*"*a)


#2439 {:>{}} : 중괄호 안에 중괄호 작성 가능 (감싸고 있는 중괄호가 {0},속해있는 중괄호가 {1})
N = int(input())
for i in range(N):
    a = i+1 # +1 한이유는 range이기 때문 (0 ~ N-1이니까)
    b = "*"*a
    print("{:>{}}".format(b, N))


#10952
while True:
    A, B = map(int, input().split())
    if (A==0 & B==0):
        break
    else: 
        print(A+B)
    

# 10951
while True:
    try:    
        A, B = map(int, input().split())
        print(A+B)
    except:
        break
