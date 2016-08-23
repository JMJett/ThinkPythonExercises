__author__ = 'Jarod Jett'


def check_fermat(a,b,c,n):

    answer = pow(a,n) + pow(b,n)
    print(pow(a,n), " + ", pow(b,n), " = ", pow(c,n), "?")
    if answer == pow(c,n):
        print("Yes. Fermat was wrong!")
    else:
        print("No. The theorem holds.")

a = int(input("Enter an integer for A: "))
b = int(input("Enter an integer for B: "))
c = int(input("Enter an integer for C: "))
n = int(input("Enter an integer greater than 2 for n: "))

check_fermat(a, b, c, n)