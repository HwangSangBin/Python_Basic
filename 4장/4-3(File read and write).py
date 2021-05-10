# 파일 읽고 쓰기

f = open("새 파일.txt", "w")
f.close()
# 파일생성 = open("파일이름", "파일열기모드")
# r = 읽기모드
# w = 쓰기모드
# a = 추가모드(마지막에 새로운 내용 추가)
f = open("새 파일.txt", "w")
for i in range(1,11):
    data = ("%d번 째 줄입니다.\n" %i)
    f.write(data)
f.close()
# 쓰기모드를 통해 쓰기
f = open("새 파일.txt", "r")
line = f.readline()
print(line)
f.close()
# 읽기모드를 통해 1줄 읽기
f = open("새 파일.txt", "r")
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()
# 읽기모드를 통해 모든 줄 읽기
f = open("새 파일.txt", "r")
lines = f.readlines()
for line in lines:
    print(line)
f.close()
# readlines는 모든 줄을 요소로 갖는 리스트로 돌려줌.
f = open("새 파일.txt", "r")
data = f.read()
print(data)
f.close()
# read는 파일 전체 읽기
f = open("새 파일.txt", "a")
for i in range(11, 20):
    data = ("{0}번 째 줄이 추가되었습니다.\n".format(i))
    f.write(data)
f.close()
# 추가모드를 통해 추가하기
with open("noop.txt", "w") as f:
    f.write("Life is too short, you need python")
# with문은 자동으로 닫아줌.
# f.close()를 생략할 수 있다는 것
