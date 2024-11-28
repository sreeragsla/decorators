def timeDecor(arg):
    def inner():
        import time
        it=time.time()
        arg()
        ft=time.time()
        print(ft-it)
    return inner
@timeDecor
def armstrong():
    ll=int(input())
    ul=int(input())
    for n in range(ll,ul+1):
        dummy=n
        p=len(str(n))
        summ=0
        while dummy>0:
            rem=dummy%10
            dummy//=10
            summ+=rem**p
        if n==summ:
              print(n)
armstrong()