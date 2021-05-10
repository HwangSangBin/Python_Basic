# Q1.   calculator를 상속하는 클래스를 만들고 값을 뺄 수 있는 minus 메서드 추가
class calculator:
    def __init__(self):
        self.value = 0
    
    def add(self, val):
        self.value += val

class Upgradecalculator(calculator):
    def minus(self, bbaegi):
        self.value -= bbaegi
cal = Upgradecalculator()
cal.add(10)
cal.minus(7)
print(cal.value)

# Q2.   객체변수 value가 100 이상의 값은 가질 수 없도록 제한하는 클래스 만들기
class MaxLimitCalculator(calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100
cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)

# Q3.   결과예측
print(all([1, 2, abs(-3)-3])) # 모두가 참이면 T, 하나라도 거짓이면 F
# 0이 존재하므로 F
chr(ord("a")) =="a"
print(chr(ord("a")))
# 아스키 코드를 기호 혹은 숫자로 바꿈
# 기호 혹은 숫자를 아스키 코드로 바꿈
# a 출력

# Q4.   fiter와 lambda를 사용하여 [1, -2, 3, -5, 8, -3]에서 음수 제거
def positive(x):
    return x> 0
print(list(filter(lambda x: x > 0, [1, -2, 3, -5, 8, -3])))

# Q5.   16진수 문자열 0xea를 10진수로 변경
# hex는 정수를 16진수로 변경
print(int(0xea))

# Q6.   map과 lambda를 사용하여 [1, 2, 3, 4]를 [3, 6, 9, 12]로 만들기
def three_times(x):
    return x*3
print(list(map(three_times, [1, 2, 3, 4])))

# Q7.   리스트의 최댓값과 최솟값
listss = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(listss))
print(min(listss))

# Q8.   반올림하기
print(round(17/3,4))

# Q12.  time을 사용하여 현재 날짜와 시간을 출력
import time
print(time.strftime("%Y/%m/%d %H:%M:%S"))

# Q13.  random 사용하여 로또번호 뽑기
import random
roddo = []
while len(roddo) < 6:
    num = random.randint(1, 45)
    if num not in roddo:
        roddo.append(num)
print(roddo)