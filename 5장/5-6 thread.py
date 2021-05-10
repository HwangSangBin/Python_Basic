# 스레드
# 보통 1개의 프로세스는 한 가지 일만 하지만 스레드를 사용하면 한 프로세스 안에서 2가지 or 그 이상의 일을 동시에 수행 가능
import time
""" def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" %i)

print("Start")

for i in range(5):
    long_task()

print("End") """
# long_task 함수는 수행하는데 5초가 걸린다.
# 5번 반복하니 25초가 걸린다.
# But 스레드를 사용하면 5초의 시간이 걸리는 함수를 동시에 실행 가능
import threading
""" def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" %i)

print("Start")

threads = []

for i in range(5):
    t = threading.Thread(target=long_task) #    스레드를 생성
    threads.append(t)

for t in threads:
    t.start()   #   스레드를 실행

print("End") """ 
# 25초 걸리던 작업이 5초 정도에 수행된다
# threading.Thread를 사용하여 만든 스레드 객체가 동시 작업을 가능하게 해줌
# start와 end가 먼저 출력되고 이후 스레드의 결과 출력, 프로그램 정상 종료 안됨
def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" %i)

print("Start")

threads = []

for i in range(5):
    t = threading.Thread(target=long_task) #    스레드를 생성
    threads.append(t)

for t in threads:
    t.start()   #   스레드를 실행

for t in threads:
    t.join()    # join으로 스레드가 종료될 때까지 기다림

print("End")