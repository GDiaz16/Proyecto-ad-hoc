import threading
def p():
    for i in range(1000):
        print(f"A {i}--------")

def q():
    for i in range(1000):
        print(f"B {i}")
t1 = threading.Thread(target = p)
t2 = threading.Thread(target = q)
t1.start()
t2.start()