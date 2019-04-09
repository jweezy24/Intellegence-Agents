import cacheTable
from distutils.core import setup
from Cython.Build import cythonize
import pyximport; pyximport.install()
#setup(ext_modules = cythonize("cacheTableWrapper.pyx"))
import cacheTableWrapper

def testing():
    cachTB = cacheTable.cacheTable("test","shit", [['a','b','c','d','e',1]])
    cacheW = cacheTableWrapper.cacheWrap(cachTB)
    print(cacheW)
testing()
