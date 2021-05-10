def add(a,b):
    return a+b

def sub(a,b):
    return a-b

if __name__ == "__main__":
    print(add(10,4))
    print(sub(9,1))
# 위 구문을 통해 다른 파일에서 모듈로 사용할 때 다른 파일에서 출력되지 않는다.

# __name__란?
# 직접 파일을 실행할 경우 __name__ 변수에는 __main__ 값이 저장된다.
# 모듈로 사용할 경우 __name__ 변수에는 mod1.py의 모듈 이름 값 mod1이 저장된다.
