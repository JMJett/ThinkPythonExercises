import time
import turtle

def timeConvert():
    """
    Converts from epoch time into Year Month Day, Hours Minutes Seconds
    Prints the number of days since Jan 1 1970
    :return:
    """
    print(time.time())
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    days = int(time.time() / 86400)
    print("It has been ", days, " days since the start of the epoch.")

def koch(t,length):
    if length < 10:
        t.fd(length)
        return
    x = length / 3
    koch(t,x)
    t.lt(60)
    koch(t,x)
    t.rt(120)
    koch(t,x)
    t.lt(60)
    koch(t,x)

def snowflake(t,length):
    for i in range(3):
        koch(t,length)
        t.rt(120)

bob = turtle.Turtle()

snowflake(bob,100)
timeConvert()

