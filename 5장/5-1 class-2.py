# 클래스의 상속
# 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만듬
# 상속을 하는 이유
# 기존 클래스를 변경하지 않고 기능을 추가하거나 변경하기 위해 사용
class fourcal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
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

class morefourcal(fourcal):
    def pow(self):
        result = self.first ** self.second
        return result
# 괄호 안에 상속할 클래스
# morefourcal은 fourcal의 모든 기능을 수행 할 수 있음
a = morefourcal(3,2)
print(a.pow())
# 제곱하기


################################################ 메서드 오버라이딩 ####################################################
# 부모 클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것
# 오버라이딩을 하면 부모 클래스의 메서드 대신 오버라이딩한 메서드가 호출됨

# a = fourcal(4,0)
# print(a.div())
# 4를 0으로 나누려고 하기 때문에 오류 발생
# But 0으로 나눌 때 오류가 아니라 0을 돌려주도록.
class safefourcal(fourcal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first/self.second
a = safefourcal(4,0)
print(a.div())


################################################## 클래스 변수 ###############################################################
# 객체 변수는 다른 객체들에 영향X, 독립적으로 그 값을 유지
class family:
    lastname = "황"
# lastname이 클래스 변수
# 클래스 변수는 클래스 안에 함수를 선언하는 것과 마찬가지로 클래스 안에 변수를 선언하여 생성
print(family.lastname)
family.lastname = "김"
print(family.lastname)