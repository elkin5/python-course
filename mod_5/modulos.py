#import sys, os
from sys import path as syspath
from os import path as ospath, getcwd

syspath.insert(0, ospath.dirname(getcwd()))
import mod_4.operaciones as op

#import operaciones as op

if __name__ == '__main__':
	print(dir(op))
	#print(syspath)
	print(op.operacion(2, 3, 4, operacion="suma"))
	print(op.operacion(2, 3, 4, operacion="producto"))