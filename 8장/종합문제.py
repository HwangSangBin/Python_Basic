# Q1.   a:b:c:d 를 a#b#c#d로 바꿔라(split 과 join 사용)
a = ("a:b:c:d")
b = a.split(":")
c = "#".join(b)
print(c)

# Q2.   딕셔너리의 a에서 "C"라는 key에 해당하는 value를 출력하는 프로그램에서 오류대신 70 얻기
try:
    a = {"A": 90, "B": 80}
    a["C"]
except KeyError:
    print(70)

# Q3.   리스트의 더하기와 extend 함수
a = [1, 2, 3]
a = a +[4, 5]
print(a)
b = [6, 7, 8]
b.extend([9,10])
print(b)
# + 와 extend 의 차이는?

# Q4.   50점 이상 점수들의 총합 구하기
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
result = 0
while A:
    mark = A.pop()
    if mark >= 50:
        result += mark 
print(result)
