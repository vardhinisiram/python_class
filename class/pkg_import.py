"""
from imp_pkg import imp_func as f1
from func import imp_func as f2
f1()
f2()
"""


import imp_pkg as ip
import func as f
from imp_pkg import PI_VALUE

ip.imp_func()
f.imp_func()
print(PI_VALUE)
print(__name__)
