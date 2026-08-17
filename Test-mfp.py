def f(x,m):
    s=''
    while x>0:
        s+=str(x%m)
        x//=m
    return s[::-1]
print(f(121,4))
print('успех')