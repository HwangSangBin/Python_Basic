# 조건문 if
# 조건을 판단하여 해당 조건에 맞는 상황을 수행


#x == y     같다
#x != y     같지 않다
#x <= y     y가 x보다 크거나 같다
#x >= y     x가 y보다 크거나 같다
#x or y     x, y 둘중 하나만 참이어도 참
#x and y    x, y 모두 참이어야 참
#not x      x가 거짓이면 참
print(1 in [1, 2, 3])
# 1이 [1, 2, 3] 안에 있니?
pocket = ["phone", "money", "goods"]
if "money" in pocket:
    print("택시 타라")
else:
    print("걸어 가라")
# if문 예시
pocket = ["phone", "money", "goods"]
if "money" in pocket:
    pass
else:
    print("걸어 가라")
# pass 활용
