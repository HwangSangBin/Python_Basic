# 문법도 어느 정도 알겠고, 책 내용도 이해했다.
# 하지만 어떻게 프로그램을 짜야할지는 모른다.
# 가장 먼저 "입력" 과 "출력"을 생각하라.
def GuGuDan(h):
    for i in range(9):
        T = i+1
        print(h*T)
result = GuGuDan(2)

# STEP 1.   구구단 프로그램 중 2단을 만든다며 2를 입력값으로 주었을 때, 어떻게 출력되어야 하는지 생각해본다.
# result = GuGu(2)

# STEP 2.   이제 결괏값을 어떻게 받을 것인가? result = [2,4,6,8,10,12,14,16,18]과 같은 형식으로 하는 게 좋겠다.는 생각을 한다.

# STEP 3.   이제 GuGu 함수를 작성해보자.
def GuGu(n):
    print(n)

# STEP 4.   결괏값을 담을 리스트 생성.
def GuGu(n):
    result = []

# STEP 5.   result 안에 숫자를 어떻게 넣을까?
def GuGu(n):
    result = []
    for i in range(9):
        E = i + 1
        H = n * E
        result.append(H)
    return result
print(GuGu(2))

# STEP 6. 위의 함수가 이상적인 구구단 함수이다.