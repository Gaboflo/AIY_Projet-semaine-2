from math import pi

'''print('hello world!! my name is Guillaume')

numun=5
numdeux=15
numun,numdeux=numdeux,numun
print(numun,numdeux)

#tempf=input()

def conversion(tempf):
    return float((tempf-32)/1.8)
print(conversion(5))


print('22/7 is greater than pi:', 22/7>pi)


string_1=str(n)
string_2=string_1*2
string_3=string_1*3
print(int(n)+int(string_2)+int(string_3))

n=input("integer value")
nn="{}{}".format(n,n)
nnn="{}{}{}".format(n,n,n)
print(int(n)+int(nn)+int(nnn))'''


'''def maxi(a,b):
    if a<=b:
        return b
    else:
        return a'''

#ex 2

def print_arguments ( a , b=3) :
        print("Arguments: {0} and {1}".format(a,b))


#ex 3

def euclidian_div(a,b,euclidian=True,remainder=False):
    if euclidian and remainder:
        return a%b
    if remainder:
        return a//b,a%b
    else:
        return a//b

#ex 5

def variadic (* args , ** kwargs ) :
    print (" Positional :", args )
    print (" Keyword :", kwargs )

#ex 6

def average(* args):
    s=0
    if len(args)==0:
        return None
    else:
        for k in range(len(args)):
            s+=args[k]
        return s/len(args)
#ex 7

def loops(n):
    L=[]
    for k in range(n):
        if k%3!=0:
            continue
        if k%5==0:
            continue
        L.append(k)
    return L




#ex 8
def is_prime(p):
    for k in range(2,p):
        if p%k==0:
            return False
    return True


#ex 9

def Hanoi_tower(n):
    if n==2:
        B.append(A[1])
        del A[1]
        C.append(A[0])
        del A[0]
        C.append(B[0])
        del B[0]
        return A,B,C

#ex 10

def sum_digit_iter(n):
    s=0
    while n!=0:
        s+=n%10
        n=n//10
    return s

def sum_digit_rec(n):
    if n//10==0:
        return n%10
    else:
        return sum_digit_rec(n//10)+n%10

#ex 11

def digital_root_iter(n):
    s=sum_digit_iter(n)
    while s//10!=0:
        s=sum_digit_iter(s)
    return s

def digital_root_rec(n):
    if n//10==0:
        return n
    else:
        return digital_root_rec(sum_digit_rec(n))

#ex 13
