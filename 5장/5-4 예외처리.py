# 예외처리

#################### try, except #######################
# try 블록 수행 중 오류가 발생하면 except 블록이 수행
# 단, try 블록에서 오류가 발생하지 않는다면 except 블록은 수행X
#try:

# except:
# 오류 종류에 관계없이 오류가 발생하면 except 수행

# except 발생 오류:
# except문에 미리 정해 놓은 오류 이름과 일치할 때만 except 블록 수행

# except 발생오류 as 오류 메시지 변수:
# 위 경우에서 오류 메시지의 내용까지 알고 싶을 때
try:
    4/0
except ZeroDivisionError as e:
    print(e)

##################### try, finally ########################
f = open("foo.txt", "w")
try:
    print("sangbin")
finally:
    f.close()
# finally절은 try문 수행 도중 예외 발생 여부에 관계없이 항상 수행
# 사용한 리소스를 close할 때 자주 사용
try:
    a =[1, 2]
    print(a[3])
    4/0
except ZeroDivisionError:
    pirnt("0으로 나눌 수 없어")
except IndexError:
    print("인덱싱할 수 없어")
# 여러 개의 오류처리
# a[3]에서 IndexError을 발생시키므로 "인덱싱할 수 없습니다"라는 문자열 출력
# 인덱싱 오류가 먼저 발생했으므로 4/0으로 발생되는 ZeroDivisionError 오류는 발생X
try:
    a =[1, 2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    pirnt(e)
except IndexError as e:
    print(e)

try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)
# 2개 이상의 오류를 동시에 처리하기 위해서 괄호로 함께 묶어 처리

######################### 오류 회피하기, 일부러 발생시키기 ###############################
try:
    f = open("나없는파일","r")
except FileNotFoundError:
    pass
# try문 안에서 FileNotFoundError가 발생한 경우에 pass를 사용하여 오류를 그냥 회피
class Bird:
    def fly(self):
        raise NotImplementedError
# Bird calss를 사속받는 자식 class는 반드시 fly 함수를 구현해야 한다는 의지를 보여준다.
# 만약 자식 class가 fly 함수를 구현하지 않은 상태로 fly 함수를 호출한다면

# class Eagle(Bird):
#    pass
# eagle = Eagle()
# print(eagle.fly())

# Eagle class는 Bird class를 상속받는다.
# 그런데 Eagle calss에서 fly 함수를 구현하지 않았기 때문에 Bird class의 fly 함수가 호출
# 그리고 rasie문에 의해 NotImplementedError가 발생
# 상속받는 class에서 함수를 재구현하는 것 = 메서드 오버라이딩
class Eagle(Bird):
    def fly(self):
        print("very fast")
eagle = Eagle()
print(eagle.fly())

######################## 예외 만들기 ########################
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == "바보":
        raise MyError
    print(nick)
say_nick("천사")
say_nick("바보")
#############################
try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")
# 예외 처리 기법을 사용하여 MyError 발생을 예외 처리
try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)
# 위를 실행하면 오류 메시지가 출력되지 않는다. 오류 메시지를 보이게 하려면 오류 class에 __str__ 메서드를 구현해야 한다.
# 86번 째 줄 원래는 pass였으나 저렇게 바꿈으로써 '허용되지 않는 별명입니다.'를 출력할 수 있게 된다.
