from functools import reduce

def prod(a):
    return reduce(lambda x,y:x*y,a)