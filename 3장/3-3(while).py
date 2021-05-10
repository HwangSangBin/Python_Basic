# 반복문 while
# while ~~:
# 무한루프 while True:


treehit = 0 
while treehit < 10:
    treehit += 1
    print("나무를 {0}번 찍었습니다.".format(treehit))
    if treehit == 10:
        print("나무 쓰러져떠")
# while문 예시
coffee = 10
money = 3000
price = 200
while money:
    order= int(input("몇 잔 드릴까?"))
    coffee -= order
    total_price = price*order
    money -= total_price
    if money >0:
        print("커피 {0}잔 드릴게요.".format(order))
        if coffee <= 0:
            print("장사 끝!")
            break
    elif money <= 0:
        print("돈이 부족해요 ㅜㅜ")
        break
    else:
        print("다시 똑바로 입력하세요.")
# 커피 자판기?
