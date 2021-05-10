# 자료형 dictionary
# key와 value를 한 쌍으로 갖는다.
# key = baseball, value = 야구
# key는 불변, value는 불변, 가변 모두 가능
# 여러 명의 사람들의 각자의 특기를 표현하기 좋음


a = {1: "a"}
a[2] = "b"
a["name"] = "sangbin"
del(a[1])
print(a)
# 추가, 삭제
grade = {"math":80, "korea":87, "english":95}
print(grade["math"])
print(grade.get("english"))
# key를 통한 value 출력
b = {1:"a", 1: "b"}
print(b[1])
# key 값을 설정해 놓으면 하나를 제외한 나머지는 모두 무시된다.
c = {"name": "sangbin", "age": "20", "birth": "010703"}
print(list(c.keys()))
print(list(c.values()))
print(list(c.items()))
c.clear()
print(c)
# key만, value만, key + value 출력
