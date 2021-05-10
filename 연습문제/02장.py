# Q1.   평균 점수 구하기
# 국어 80, 영어 75, 수학 55
korean, english, math = (80, 75, 55)
total = korean + english + math
average = total/3
print(average)

# Q2.   13이 홀수인지 짝수인지 판별할 수 있는 방법
number = 13
remainder = number%2
if remainder == 1:
    print("홀수입니다.")
else:
    print("짝수입니다.")

# Q3.   주민등록번호 881120-1068234에서 연월일 부분과 그 뒤의 숫자 부분으로 나누어 출력
# 슬라이싱 사용
identification = "881120-1068234"
YMD = "19" + identification[:6]
print(YMD)
print(identification[7:])

# Q4.   주민등록번호 881120-1068234에서 성별을 나타내는 숫자 출력
# 인덱싱 사용
identification = "881120-1068234"
print(identification[7])

# Q5.    문자열 a:b:c:d  replace 사용하여 a#b#c#d로 출력
a = ("a:b:c:d")
print(a.replace(":","#"))

# Q6.   [1, 3, 5, 4, 2]를 [5, 4, 3, 2, 1]로 바꾸기
# 리스트의 내장 함수 사용
a = [1, 3, 5, 4, 2]
a.sort() # 크기순 정렬
a.reverse() # 뒤로 정렬
print(a)

# Q7.    ["Life", "is", "too", "short"]를 Life is too short 문자열로 출력
# join 함수 사용?
a = ["Life", "is", "too", "short"]
print(a[0], end = " ")
print(a[1], end = " ")
print(a[2], end = " ")
print(a[3])

###################################################################################################
# Q8.    (1, 2, 3) 튜플에  값 4 추가하기
a = (1, 2, 3)
a = a + (4,)
print(a)
###################################################################################################

# Q9.   딕셔너리 A 오류가 발생하는 경우는?
a= dict()
print(a)
#a[[1]] = "python"
# why? dictionary ㅣ로는 변하는 값을 사용 불가능 

# Q10.   딕셔너리 a에서 'B'에 해당되는 값 추출
a = {'A':90, "B": 80, "C": 70}
print(a["B"])

# Q11.   a 리스트에서 중복 제거
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
a = set(a)
print(a)

# Q12.   a,b 변수 선언 후, a의 두 번째 값 변경하면 b 어케 되누?
a = b = [1, 2, 3]
a[1]= 4
print(b)
# 똑같이 바뀜 a, b 모두 동일한 리스트 객체를 가리키고 있기 때문