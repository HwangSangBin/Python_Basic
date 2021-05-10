# Q1.   코드의 결과 값?
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
# 가장 먼저 참이 되는 것이 3번 째 조건이므로 "shirt"가 출력

# Q2.   while을 통해 1~100까지 3의 배수의 합
num = 0
suum = 0
while num < 1000:
    num += 1
    nado = num + 1
    if nado%3 ==0:
        suum += nado
    else:
        pass
print(suum)

#Q3.     while을 통해서 * 계단타기
num =0
while num <5:
    num += 1
    print("*"*num)

#Q4.    for을 통해서 1~100 출력
num = 0
for i in range(100):
    num += 1
    print(num)

#Q5.    for을 이용해서 평균 점수
score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
suum = 0
for i in score:
    suum += i 
    suum1 = suum/10
print(suum1)

#Q6.    리스트 중에서 홀수에만 2를 곱하여 저장하는 코드를 리스트 내포 사용하기
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n%2 ==1:
        result.append(n*2)
###############################
numbers2 = [1, 2, 3, 4, 5]
results = [n*2 for n in numbers2 if n%2 ==1]
print(results)