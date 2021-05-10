# Q1.   홀짝 구분 할 수 있는 함수
def is_odd(number):
    if number%2 == 0:
        return True
    else:
        return False
print(is_odd(5))

# Q2.   입력한 모든 수들의 평균을 구해주는 함수
def averge(*num_ber):
    result = 0
    for i in num_ber:
        result += i
    return result / len(num_ber)
print(averge(40,5,30,20))

# Q3.   두 개의 숫자를 입력받아 더하여 돌려주는 프로그램
num1 = input("숫자 넣엉:")
num2 = input("숫자 또 넣엉:")
total = int(num1) + int(num2)
print("두 수의 합은" , str(total))

# Q4.   출력 결과가 다른 것 골라
# print("you" "need" "python")
# print("you" + "need" + "python")
print("you", "need", "python")
# print("".join(["you" , "need" , "python"]))

# Q5.   파일 만들고 내용물 출력
f1 = open("test.txt", "w")
f1.write("Life is too short")
f1.close()
f2 = open("test.txt", "r")
print(f2.read())

# Q6.   사용자의 입력을 파일에 저장하는 프로그램
ff = open("써라 써", "a")
fy = input("쓰세요:")
ff.write(fy)
ff.close()
fff = open("써라 써", "r")
print(fff.read())

# Q7.   문자 체인지
f3 = open("Life", "w")
f3.write("Life is too short\n you need java")
f3.close()
f3 = open("Life", "r")
body = f3.read()
f3.close()
body = body.replace("java", "python")
f3 = open("Life", "w")
f3.write(body)
f3.close()
f3 = open("Life", "r")
print(f3.read())