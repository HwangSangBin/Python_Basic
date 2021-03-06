# 문자열 포매팅

print("현재 온도는 %d 도입니다." %13)
print("오늘의 날씨는 %s입니다." %"맑음")
# %d 는 숫자, %s 는 문자열을 대입할 때 쓰는 것

number = 10
print("현재 핸드폰의 배터리는 %d%%입니다." %number)
# %를 출력하고 싶을 때는 %%를 사용한다.
string = "삼겹살"
print("%s %d인분 주세요." %(string, number))
print("%10s" %"hi")
# 10칸인 문자열 공간에서 오른쪽 정렬
print("%-10s jane." %"hi")
# 10칸인 문자열 공간에서 hi는 왼쪽을 채우고 나머지는 공백으로 채운 후, 다음 문자 출력
print("%0.4f" %3.12321321321)
# 소수점 4번째까지 표시
print("%10.4f" %3.434347573)
# 10칸인 문자열 공간에서 소수점 4번째까지 표시하고 오른쪽 정렬

#################################################################################################

# .format 함수 활용 
# 이게 위에 보다 훨씬 편함

print("I like {0}.".format("pizza"))
print("I have a {0} pens.".format(4))
eat = "pizza"
can_eat = 4
print("I can eat {0} {1}.".format(can_eat, eat))
print("{0:<10}".format("hi"))
# 10칸 중에서 왼쪽 정렬
print("{0:>10}".format("hi"))
# 10칸 중에서 오른쪽 정렬
print("{0:^10}".format("hi"))
# 10칸 중에서 가운데 정렬
print("{0:=^10}".format("hi"))
# 공백 채우기
print("{0:0.4f}".format(3.1467854))
# 소수 표현하기