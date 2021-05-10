# 자료형 List
# 리스트의 항목 값은 변화 가능

a = [1, 2, 3, ["b", "c", "d"]]
print(a[3])
print(a[1])
print(a[-1])
print(a[3][1])
print(a[-1][0])
b = [4, 5, 6, 7, 8, 9]
print(a+ b)
# 리스트 추가
print(b*3)
# 리스트 반복
print(len(b))
# 리스트 길이 구하기
b[2] = "d"
print(b)
# 리스트 값 수정
del b[0]
print(b)
# 리스트 값 제거
del b[:4]
print(b)
# 슬라이싱 기법을 통한 리스트 값 제거
b.append(11)
b.append([14, 15])
print(b)
# 리스트 값 추가 append는 하나씩만 추가 가능
r = [1, 3, 9, 5, 7, 2, 2]
t = ["a", "t", "g", "r"]
r.sort()
t.sort()
print(r)
print(t)
# 숫자열, 문자열 정렬
r.reverse()
t.reverse()
print(r)
print(t)
# 거꾸로 정렬
r.insert(0,7)
print(r)
# 0번째 자리에 7이라는 숫자 삽입
r.remove(7)
print(r)
# 7이라는 숫자 제거, 두 개 이상이 있으면 첫 번째 7만 제거
r.pop()
print(r)
# 맨 뒤에 있는 요소 삭제
r.pop(0)
print(r)
# 0번째 자리에 있는 요소 삭제
print(r.count(2))
print(r.count(3))
# 리스트 안에 있는 요소의 개수 세기
q = [1, 2, 3]
q.extend([4, 5])
print(q)
b = [6, 7]
q.extend(b)
print(q)
# 리스트 확장 시키기
