# 함수
# 사용하는 이유: 똑같은 내용을 반복하는 것을 줄여줌
# "어떤 입력 값을 주었을 때 어떤 결과 값을 준다" 라는 식의 함수로 작성하는 것이 현명

# 매개변수(parameter): 함수에 입력으로 전달된 값을 받는 변수
# 인수(arguments): 함수를 호출할 때 전달하는 입력값

def plus(a, b):                 # a, b는 매개변수
    return a+b
c= plus(3,4)                    # 3, 4는 인수
print(c)
# 입력값: a, b
# 결과값: a + b 
# return은 함수의 결괏값을 돌려주는 명령어

def say():
    print("Hi")
z = say()
# 입력값이 없는 함수
def add(a,b):
    print("%d, %d의 합은 %d입니다."%(a,b,a+b))
a = add(5,6)
# 결괏값이 없는 함수
# "문자가 출력되었는데 왜 결괏값이 없지?"라고 의문을 가질 수 있다.
# print문은 함수의 구성 요소 중 하나인 <수행할 문장>에 해달하는 부분일 뿐 결괏값이 아니다.
# 결괏값은 오직 return 명령어로만 돌려받을 수 있다.
print(z)
print(a)
# 결괏값이 없는 함수를 하나에 변수에 넣고 print를 통해 출력하면 None가 출력된다.
def add_many(*args):
    all_plus = 0
    for i in args:
        all_plus += i
    return all_plus
p = add_many(1,2,3,4,5)
print(p)
pp = add_many(1,2,3,4,5,6,7,8,9,10)
print(pp)
# *args처럼 매개변수 이름 앞에 *를 붙이면 입력값을 전부 모아서 튜플로 만들어준다.
# *args는 *sang *bin *sangbin 모두 같은 표현이다.
# args 자주 사용
def add_mul(choice, *sangbin):
    if choice =="add":
        result = 0
        for i in sangbin:
            result += i
    elif choice == "mul":
        result = 1
        for i in sangbin:
            result *= i
    return result
result = add_mul("add",1,2,3,4,5)
print(result)
result = add_mul("mul",1,2,3,4,5)
print(result)
# 예제
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1)
print_kwargs(name = "sangbin", age = 20)
# 키워드 피라미터: 매개변수 앞에 **을 사용
# 입력값 모두 key = value 형태의 딕셔너리로 출력된다.
# kwargs 자주 사용
def add_and_mul(a,b):
    return a+b, a*b
result = add_and_mul(3,4)
print(result)
result1, result2 = add_and_mul(6,8)
print(result1)
print(result2)
##########################################################################################################
##########################################################################################################
#                                                       중요함
# 함수의 결괏값은 언제나 하나.
# 위처럼 두 개를 리턴하면 튜플의 형태로 출력된다.
# 나누기도 가능함.
##########################################################################################################
##########################################################################################################
a =1
def vartest(a):
    a += 1
vartest(a)
print(a)
# 2가 나올 거 같지만 1이 나온다.
# 그 이유는 함수 안에 새로 만든 매개변수는 "함수만의 변수"이기 때문이다.
a =1
def vartest(a):
    a += 1
    return a
a= vartest(a)
print(a)
# return을 통해 함수 밖의 변수 변경
# 여기서도 함수 안의 'a'와 밖의 'a'는 다르다.
a = 1
def vartest():
    global a
    a += 1
vartest()
print(a)
# global을 통한 변경
# 함수는 독립적으로 존재하는 것이 좋기에 좋은 방법은 아님
add = lambda a,b: a+b
result = add(3,4)
print(result)
#################################################################
def add(a,b):
    return a+b
result= add(3,4)
print(result)
# 두 식은 같은 뜻이다.
# lambda는 함수를 생성할 때 사용하는 예약어
# def와 동일한 역할
# def 사용할 정도로 복잡하지 않거나, 사용할 수 없을 때 주로 사용함
