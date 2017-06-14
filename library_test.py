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

f2_proto = CFUNCTYPE(c_void_p)
f2_params = (1, "s1", 0)
f2_c = f2_proto(("f2", hllDll))

class struct1(Structure):
    _fields_ = [("a", c_int*3), ("b", c_int*3)]

def f2_test():
    print 'Test f2'
    a = (c_int*3)()
    b = (c_int*3)()

    a[0] = 1
    b[0] = 2

    s1 = struct1()
    s1.a = a
    s1.b = b

    print 'Before: ',  s1.a[0], s1.b[0]

    f2_c(pointer(s1))

    print 'After: ',  s1.a[0], s1.b[0]

f1_test()

f2_test()