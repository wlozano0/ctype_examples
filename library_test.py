import ctypes
import time

from ctypes import *

path = 'debug\\'

hllDll = CDLL(path + "library.dll")

f1_proto = CFUNCTYPE(c_void_p)
f1_params = (1, "a1", 0)
f1_c = f1_proto(("f1", hllDll))

def f1_test():
    print 'Test f1'
    a1 = (c_int*3)()
    a1[0] = 1
    a1[1] = 2
    a1[2] = 3

    print 'Before: ', a1[0], a1[1], a1[2]

    f1_c(pointer(a1))

    print 'After: ', a1[0], a1[1], a1[2]

f1_test()