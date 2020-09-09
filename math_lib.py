import numpy

def div(a, b):
    if b == 0:
        print("Warning! \n Denominator cannot be zero")
        return numpy.inf
    else:
        return (a/b)

def add(a, b):
    return (a+b)