import time
import threading


def mat_op(a):
    print(a)
    time.sleep(1)


thr1 = threading.Thread(
    target=mat_op,
    args=(2+2,),
    name='thr-1'
    )
thr2 = threading.Thread(
    target=mat_op,
    args=(2-2,),
    name='thr-2'
    )
thr3 = threading.Thread(
    target=mat_op,
    args=(2*2,),
    name='thr-3'
    )

t1 = time.time()

thr1.start()
thr2.start()
thr3.start()

thr1.join()
thr2.join()
thr3.join()

t2 = time.time()

print(t2-t1)
