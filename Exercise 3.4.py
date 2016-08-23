__author__ = 'Jarod Jett'

def do_twice(f, arg):
    f(arg)
    f(arg)


def print_spam(arg):
    print(arg)

do_twice(print_spam, 'string')
print('')

def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)

do_four(print_spam, 'spam')
print('')