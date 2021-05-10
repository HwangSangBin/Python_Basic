# 외장 함수

# sys
# 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
# 딱히 쓸 때 없어 보임

# pickle
# 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈
import pickle
f = open("20200520.txt", "wb")
data = {1: "상", 2: "빈"}
pickle.dump(data, f)
f.close()
# 다음 예는 pickle 모듈의 dump 함수를 사용하여 딕셔너리 개체인 data를 그대로 파일에 저장하는 방법
f = open("20200520.txt", "rb")
data = pickle.load(f)
print(data)
# pickle.dump로 저장한 파일을 pcikle.load를 사용해서 원래 있던 딕셔너리 객체(data) 상태 그대로 불러오는 예

# OS
# 환경 변수나 디렉터리, 파일 등의 OS자원을 제어
import os 
print(os.environ) # 내 시스템의 환경 변수값을 알고 싶을 때
os.chdir("C:\WINDOWS") # 디렉터리 위치 변경
print(os.getcwd) # 디렉터리 위치 돌려받기
print(os.system("dir")) # 시스템 명령어 호출
h = os.popen("dir") # 실행한 시스템 명령어의 결괏값 돌려받기
print(h.read()) # 읽어 들인 파일 객체의 내용 보기
os.mkdir # 디렉터리 생성
os.rmdir # 디렉터리 삭제, 단 디렉터리가 비어있어야함
os.unlink # 파일을 지운다
# os.rename(src, dst) # src라는 이름의 파일을 dst라는 이름으로 바꾼다
# shutil
# 파일 복사
# src라는 이름의 파일을 dst로 복사
# if dst가 디렉터리 이름이라면 src라는 파일 이름으로 dst 디렉터리에 복사하고 동일한 파일 이름이 있을 경우 덮어쓴다
import shutil
# shutil.copy("src.txt", "dst.txt")

# glob
# 특정 디렉터리에 있는 파일 이름 모두를 알아야 할 때 사용
import glob
print(glob.glob("C:\\Users\\tkdql\\Desktop\\python place/p*"))

# tempfile
# 파일을 임시로 만들어서 사용할 때 유용함
import tempfile
filename = tempfile.mkstemp() # 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 돌려줌
print(filename)
f =tempfile.TemporaryFile() # 임시 저장 공간으로 사용할 파일 객체를 돌려줌 기본적으로 바이너리 쓰기 모드(wb)를 갖는다
f.close() # 이것을 호출하면 파일 객체는 자동으로 사라진다

# time
# 시간 관련
import time
print(time.time()) # 현재 시간을 실수 형태로 돌려줌, 1970년1월1일0시0분0초 기준으로 지난 시간을 초 단위로
print(time.localtime(time.time())) # 연 월 일 시 분 초 형태로 바꾸어줌
print(time.asctime(time.localtime(time.time()))) # localtime의 값을 인수로 받아 보기 쉽게 변형
print(time.ctime()) # 항상 현재 시간만 돌려줌
print(time.strftime("%a, %b, %c, %d, %H", time.localtime(time.time()))) # 여러 가지 포맷 코드 제공
for i in range(1):
    print(i)
    time.sleep(1)
# 1초 간격으로 0부터 9초까지 숫자를 출력, 실수 형태로 쓸 수 있다.

# calendar
# 달력
import calendar
print(calendar.calendar(2020))
print(calendar.prcal(2020)) # 위와 같음
print(calendar.prmonth(2020, 5))
print(calendar.weekday(2020,5, 20)) # 월화수목금토일 0123456
print(calendar.monthrange(2020,5)) # 달의 1일이 무슨 요일인지 며칠까지 있는지 튜플 형태

# random
# 랜덤함수
import random
print(random.randint(1, 10)) # 1~10 정수 중 난수 값
data = [1,2,3,4,5]
random.shuffle(data)
print(data)

# webbrowser
# 자신의 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈
import webbrowser
webbrowser.open("http://google.com") # 이미 창이 있으면 입력창으로 이동 
# 새로운 창을 원한다면 open_new 사용
