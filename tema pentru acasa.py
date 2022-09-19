a=int(input("Primul nr:"))
b=int(input("Al doilea nr:"))
# a)
def suma(a,b):
    return(a+b)
print("Suma:", suma(a,b))
# b)
def produs(a,b):
    return(a*b)
print("Produsul:",produs(a,b))
# c)
def med_aritm(a,b):
    m=(a+b)/2
    return(m)
print("Media aritmetica a numerelor:",med_aritm(a,b))
# d,e)
def cmmdc(m,n):
    while m!=n:
        if m>n: m=m-n
        else: n=n-m
        return(m)
m=int(input("m="))
n=int(input("n="))
print("Cel mai mare divizor comun:",cmmdc(m,n))
print("Cel mai mic multiplu comun:",str(m*n//cmmdc(m,n)))
# f)
def minimul(a,b):
    return(min(a,b))
print("Numarul minim:",minimul(a,b))
# g)
def maximul(a,b):
    return(max(a,b))
print("Numarul maxim:",maximul(a,b))
# h)
def suma_2():
    a=int(input("introduceti nr.a:"))
    b=int(input("introduceti nr.b:"))
    c=0
    c=a+b
    return(c)
s=suma_2()
print("Suma sub forma a+b=c este:",s)
# i)
def produs_2():
    a=int(input("introduceti nr.a:"))
    b=int(input("introduceti nr.b:"))
    c=1
    c=a*b
    return(c)
p=produs_2()
print("Produsul sub forma a*b=c este:",p)
# j)
n=int(input("introdu n:"))
m=int(input("introdu m:"))
def divizori_comuni(x,y):
    w=[]
    if x<y:
        for i in range(1,x+1):
            w.append(i)
    elif y<x:
        for z in range(1,y+1):
            if y%z==0 and x%z==0:
                w.append(z)
    else:
        for q in range(1,x+1):
            if x%q==0:
                w.append(q)
    print("lista divizorilor comuni:",w)
    return(w)
divizori_comuni(n,m)
# k)
# l)
def cifre_in_2numere():
    a=str(input("introduceti nr.a:"))
    b=str(input("introduceti nr.b:"))
    vd=[]
    for i in range(0,len(a)):
        if a[i] in b:
            vd.append(a[i])
    return vd
srt=cifre_in_2numere()
print("Cifrele care sunt in cele 2 numere:")
# m)
# n)