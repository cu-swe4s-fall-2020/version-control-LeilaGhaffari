
import math_lib as ml

def calc(x, y):

    add = ml.add(x, y)
    div = ml.div(x, y)
    print ("add = ", add, "\ndivide = ", div)
    return

if __name__ == '__main__':
    calc(4,3)