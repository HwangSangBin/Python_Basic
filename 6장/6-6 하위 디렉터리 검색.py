# 모든 파일 구하기
import os
def search(dirname):
    filenames = os.listdir(dirname)
    # 해당 디렉터리에 있는 파일들의 리스트를 구함.
    # 구하는 파일 리스트는 파일 이름만 포함되어 있으므로 경로를 포함한 파일 이름을 구하기 위해서는 dirname을 덧붙여줘야 한다.
    for filename in filenames:
        full_filename = os.path.join(dirname, filename) # 디렉터리를 포함한 전체 경로를 쉽게 구할 수 있다.
        print(full_filename)
search("c:/")

# 확장자가 .py인 파일만 출력
def search_1(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        ext = os.path.splitext(full_filename)[-1] # 이 함수는 확장자를 기준으로 두 부분으로 나눔. 확장자만 추출하기 위한 함수.
        if ext == ".py":
            print(full_filename)
search_1("c:/")

# c:/ 바로 밑 파일뿐만 아니라 그 하위 디렉터리를 포함한 모든 .py 파일을 검색하는 것이다.
def search_2(dirname):
    try:
    # try ~ except를 사용한 이유는 os.listdir를 수행할 때
    # 권한이 없는 디렉터리에 접근하더라도 프로그램이 오류로 종료되지 않고 그냥 수행
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename): # full_filename이 디렉터리인지 파일인지 구별하기 위한 것
                search_2(full_filename) # 디렉터리일 경우 해당 경로를 입력받아 다시 search함. 이러면 계속 하위 디렉터리에 접근
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == ".py":
                    print(full_filename)
    except PermissionError:
        pass
search_2("c:/")

# 더 쉽게
for (path, dir, files) in os.walk("c:/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == ".py":
            print("%s/%s" % (path, filename))
            