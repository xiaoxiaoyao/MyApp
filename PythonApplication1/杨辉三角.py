#杨辉三角
def triangles(l=1):
    Ltriangles=[1]
    while len(Ltriangles) <= l:
        yield([a for a in Ltriangles])
        for n in range(len(Ltriangles)-1):
            Ltriangles[n]=Ltriangles[n]+Ltriangles[n+1]
        Ltriangles.insert(0,1)


def triangles2(l=1):
    b = [1]
    while True:
        yield(b)
        b = [1] + [b[i] + b[i+1] for i in range(len(b)-1)] + [1]
        if len(b) >= l:
            return(0)

num=0
num=int(input('input Number:'))
a=[x for x in triangles(num)]
print(a)