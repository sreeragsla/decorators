def timeDecor(arg):
    def inner():
        import time
        it=time.time()
        arg()
        ft=time.time()
        print(ft-it)
    return inner
@timeDecor
def fibo():
    fn=int(input())
    sn=int(input())
    n=int(input('how many elements you want'))
    if n==1:
        print(fn)
    elif n==2:
        print(sn)
    else:
        print(fn)
        print(sn)
        for i in range(n-2):
            tn=fn+sn
            print(tn)
            fn,sn=sn,tn
fibo()