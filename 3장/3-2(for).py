# 반복문 for
#for 변수 in ~~:


for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end = " ")
    print(" ")
#구구단
points = (90, 25, 67, 31, 78)
num = 0
for point in points:
    num += 1
    if point < 60:
        continue
    print("축하합니다. {0}번 째 학생 합격입니다.".format(num))
# continue 활용
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
print(result)
##################################
a = [1, 2, 3, 4]
result = [sor*3 for sor in a if sor%2 ==0]
print(result)
# 리스트 내포 사용
# 표현식 for 항목 in 반복가능객체 if 조건문
