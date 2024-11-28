def dWError(arg):
    def inner(a,b):
        if b==0:
            arg(b,a)
        else:
            arg(a,b)

    return inner
@dWError
def division(a,b):
    print(a/b)

division(10,2)
division(10,0)