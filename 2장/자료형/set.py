# 자료형 set
# 중복 허용 X
# 순서 X
# set에 저장된 값을 인덱싱으로 접근하려면 리스트 or 튜플로 변환 후 접근해야함

s1 = set([1, 2, 3])
s2 = set("hello")
s3 = set()
print(s1)
print(s2)
print(s3)
# set 출력
s1 = set([1, 2, 3, 4, 5 ,6])
s2 = set([5, 6, 7, 8, 9])
print(s1 & s2)
print(s1.intersection(s2))
# 교집합
print(s1 | s2)
print(s1.union(s2))
# 합집합
print(s1.difference(s2))
print(s2.difference(s1))
# 차집합
s3 = set([1, 2, 3])
s3.add(4)
print(s3)
# 1개 값 추가하기
s3.update([5, 6, 7])
print(s3)
# 여러 개 값 추가하기
s3.remove(1)
print(s3)
# 제거하기
