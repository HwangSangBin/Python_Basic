# Class
# 클래스로 만든 것을 객체
# 클래스의 입장에서 객체는 클래스의 인스턴스
result1 = 0
result2 = 0
def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result += num
    return result2
# 함수로 표현한 2대의 계산기
class calculator:
    def __init__(self):
        self.result = 0

    def add(self,num):
        self.result += num
        return self.result
cal1 = calculator() # 객체1 
cal2 = calculator() # 객체2 
print(cal1.add(4))
print(cal1.add(4))
print(cal2.add(5))
print(cal2.add(8))
# class를 통한 2대의 계산기
class fourcal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add0(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result
# 사칙연산 기능을 가진 클래스

# 클래스 안에 구현된 함수 = 메서드
# setdata는 메서드
# a = fourcal()
# a.setdata(4,2)
# self에는 메서드를 호출한 a가 자동으로 전달됨
# b = fourcal()
# b.setdata(3,6)
# a 속 값과 b 속 값은 독립적으로 존재하므로 영향을 받지 않고 워래 값을 유지한다.
c = fourcal(4,1)
print(c.add0())