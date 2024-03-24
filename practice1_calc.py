#1000
# split() : input으로 받은 문자열을 공백을 기준으로 나누어 리스트로 만듦 (ex. 10 20 입력시 ["10", "20"] 으로 변환)
# map(function, iterable) : 반복가능한 객체에 function을 적용한 결과를 담은 map객체를 반환 
# map(int, input().split()) : split()으로 나눈 문자열 리스트의 각 원소를 int형으로 변환 (ex. ["10","20"]이 [10,20]으로 변환됨)
a, b = map(int, input().split()) 
print((a+b))
print((a-b))
print((a*b))
print(int(a/b))
print((a%b))

#10926
def CheckID(id):
    if id.isalpha(): #이 문자가 알파벳인가
        if id.islower(): #이 문자가 소문자인가
            if len(id) <= 50: #이 문자가 50자를 안 넘는가
                return True
            
id = input()
result = CheckID(id)
if result:
    print(id+"??!")


#18108
y = int(input())
seoki = y-543
print(seoki)

            

#10430
A, B, C = map(int, input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)                                     
print(((A%C) * (B%C))%C)


#2588
a = int(input())
b = int(input())

c= (b-(int(b/10)*10))
e= (int(b/100))
d=(int((b-e*100-c)/10))
print(a*c)
print(a*d)
print(a*e)
print((a*c)+(a*d*10)+(a*e*100))


#11382
A, B, C = map(int, input().split())
print(A+B+C)


#10171
print("\    /\ ")
print(" )  ( ')")
print("(  /  )")
print(" \(__)|")


